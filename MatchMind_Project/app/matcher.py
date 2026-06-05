import re
from collections import Counter
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity


def top_overlapping_terms(job_tokens, resume_tokens, limit=8):
    job_counts = Counter(job_tokens)
    resume_counts = Counter(resume_tokens)
    overlap = job_counts.keys() & resume_counts.keys()
    ranked = sorted(overlap, key=lambda term: (job_counts[term] + resume_counts[term], term), reverse=True)
    return ranked[:limit]


def rank_resumes(job_description, resumes):
    """
    Rank resumes against a job description using TF-IDF weighted cosine similarity.

    Args:
        job_description: String containing the target role requirements.
        resumes: List of dictionaries with "name" and "text" keys.

    Returns:
        List of ranked dictionaries with score, percent, rank, and matched terms.
    """
    # Prepare raw texts for TF-IDF vectorization
    job_text = job_description
    resume_texts = [resume["text"] for resume in resumes]

    # Vectorize using sklearn's TfidfVectorizer (handles tokenization, stop words, tf-idf)
    # Use scikit-learn's built-in English stop words
    vectorizer = TfidfVectorizer(stop_words="english")
    tfidf_matrix = vectorizer.fit_transform([job_text] + resume_texts)

    # Compute cosine similarity between job (row 0) and each resume (rows 1..)
    sims = cosine_similarity(tfidf_matrix[0:1], tfidf_matrix[1:]).flatten()

    # For matched terms, derive tokens using the vectorizer's analyzer
    analyzer = vectorizer.build_analyzer()
    job_tokens = analyzer(job_text)
    resume_tokens = [analyzer(text) for text in resume_texts]

    ranked = []
    for resume, score, tokens in zip(resumes, sims, resume_tokens):
        ranked.append(
            {
                "name": resume["name"],
                "score": float(score),
                "percent": round(float(score) * 100, 2),
                "matched_terms": top_overlapping_terms(job_tokens, tokens),
                "text_preview": resume["text"][:280].strip(),
            }
        )

    ranked.sort(key=lambda item: item["score"], reverse=True)
    for index, item in enumerate(ranked, start=1):
        item["rank"] = index
    return ranked
