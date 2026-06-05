# MatchMind: NLP-Powered Recruitment Matching

MatchMind is a prototype recruitment screening system for the Y Combinator-style project proposal. It ranks resumes against a job description using text extraction, TF-IDF weighting, and cosine similarity so recruiters can identify high-fit candidates faster than keyword-only filtering.

## Business Perspective

MatchMind targets boutique staffing agencies, campus recruiters, and SMEs that face high applicant volume but cannot afford slow enterprise ATS deployments. The proposed business model combines SaaS subscriptions, enterprise integration services, and pay-per-scan credits for seasonal hiring spikes.

## Technical Perspective

The prototype contains a pure Python matching engine and a Flask web interface:

- Input: job description plus multiple resume files.
- Text extraction: TXT support by default, with optional PDF and DOCX extraction through dependencies.
- NLP feature extraction: normalized tokens, TF-IDF vectors, and cosine similarity.
- Output: ranked candidates, match percentage, and overlapping skill terms.

## Setup

```bash
python -m venv .venv
.venv\Scripts\activate
pip install -r requirements.txt
python run.py
```

Open `http://127.0.0.1:5000` in a browser.

## Sample Run

Use `sample_data/job_description.txt` as the job description and upload the text files in `sample_data/resumes`.



## Project Structure

```text
MatchMind_Project/
  app/
    matcher.py
    document_loader.py
    templates/index.html
    static/style.css
  sample_data/
    job_description.txt
    resumes/
  tests/
  Project_Report.md
  README.md
  requirements.txt
  run.py
```
