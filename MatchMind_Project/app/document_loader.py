from pathlib import Path
from tempfile import NamedTemporaryFile


def _read_bytes(file_or_path):
    if hasattr(file_or_path, "read"):
        stream = getattr(file_or_path, "stream", file_or_path)
        stream.seek(0)
        return file_or_path.read()
    return Path(file_or_path).read_bytes()


def _filename(file_or_path):
    if hasattr(file_or_path, "filename"):
        return file_or_path.filename
    return str(file_or_path)


def extract_text_from_file(file_or_path):
    name = _filename(file_or_path)
    suffix = Path(name).suffix.lower()

    if suffix == ".txt":
        return _read_bytes(file_or_path).decode("utf-8", errors="ignore")

    if suffix == ".pdf":
        try:
            import pdfplumber
        except ImportError as exc:
            raise RuntimeError("PDF support requires pdfplumber. Install it or use TXT files.") from exc
        from io import BytesIO

        with pdfplumber.open(BytesIO(_read_bytes(file_or_path))) as pdf:
            parts = []
            for page in pdf.pages:
                text = page.extract_text()
                if text:
                    parts.append(text)
        return "\n".join(parts)

    if suffix == ".docx":
        try:
            import docx2txt
        except ImportError as exc:
            raise RuntimeError("DOCX support requires docx2txt. Install it or use TXT files.") from exc
        if hasattr(file_or_path, "read"):
            with NamedTemporaryFile(suffix=".docx", delete=False) as temp_file:
                temp_path = Path(temp_file.name)
                temp_file.write(_read_bytes(file_or_path))
            try:
                return docx2txt.process(str(temp_path))
            finally:
                temp_path.unlink(missing_ok=True)
        return docx2txt.process(str(file_or_path))

    raise RuntimeError(f"Unsupported file type: {suffix}. Use TXT, PDF, or DOCX.")
