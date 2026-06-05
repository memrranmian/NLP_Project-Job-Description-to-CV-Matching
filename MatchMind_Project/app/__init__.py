def create_app():
    from flask import Flask, render_template, request

    from .document_loader import extract_text_from_file
    from .matcher import rank_resumes

    app = Flask(__name__)
    app.config["MAX_CONTENT_LENGTH"] = 12 * 1024 * 1024

    @app.route("/", methods=["GET", "POST"])
    def index():
        results = []
        error = None
        job_description = ""

        if request.method == "POST":
            job_description = request.form.get("job_description", "").strip()
            files = request.files.getlist("resumes")
            resumes = []

            try:
                if not job_description:
                    raise RuntimeError("Please paste a job description before ranking resumes.")
                if not files or all(not file.filename for file in files):
                    raise RuntimeError("Please upload at least one resume file.")

                for file in files:
                    if not file.filename:
                        continue
                    text = extract_text_from_file(file)
                    resumes.append({"name": file.filename, "text": text})

                results = rank_resumes(job_description, resumes)
            except Exception as exc:
                error = str(exc)

        return render_template(
            "index.html",
            results=results,
            error=error,
            job_description=job_description,
        )

    return app
