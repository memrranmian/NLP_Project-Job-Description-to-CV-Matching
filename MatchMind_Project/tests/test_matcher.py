from app.matcher import rank_resumes


def test_best_resume_ranks_first():
    job = "Python NLP TF-IDF cosine similarity Flask resume screening"
    resumes = [
        {"name": "business.txt", "text": "sales pricing customer discovery"},
        {"name": "technical.txt", "text": "Python Flask NLP TF-IDF cosine similarity"},
    ]

    results = rank_resumes(job, resumes)

    assert results[0]["name"] == "technical.txt"
    assert results[0]["score"] > results[1]["score"]


def test_empty_resume_gets_zero_score():
    results = rank_resumes("Python NLP", [{"name": "blank.txt", "text": ""}])

    assert results[0]["score"] == 0.0
