# Job Description and CV Matching System

This project aims to build a job description and resume matching system using Python with machine learning techniques. The system helps streamline the recruitment process by automatically matching job descriptions with submitted resumes, providing recruiters with a more efficient way to identify suitable candidates.

## 🚀 Key Features

- **Job Description Input**: Recruiters can input detailed job descriptions directly into the system.
- **Resume Upload**: Supports multiple resume uploads (PDF, DOCX, and TXT) for batch matching.
- **Machine Learning Algorithm**: Utilizes TF-IDF Vectorization and Cosine Similarity to calculate precise matching scores between jobs and candidates.
- **Result Presentation**: Matched resumes are presented to recruiters with similarity scores and relevant details in a clear, ranked list.
- **Web Interface**: A clean, responsive UI built with Flask and Bootstrap for an intuitive user experience.

## 🛠️ Technologies Used

- **Python**: Backend development using the Python programming language.
- **Flask**: A lightweight web framework for building the backend server and handling HTTP requests.
- **Bootstrap**: Frontend design and layout for a responsive and user-friendly UI.
- **Machine Learning Libraries**: Libraries such as **scikit-learn** for implementing text similarity algorithms.
- **File Parsing**: **PyPDF2** and **docx2txt** for extracting text from different file formats.
- **HTML/CSS**: Frontend markup and styling for the web interface.

## 📦 Installation

1. **Clone the Repository**
   ```bash
   git clone https://github.com/memrranmian/Job-Description-to-CV-Matching.git
   cd Job-Description-to-CV-Matching
   ```

2. **Install Dependencies**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run the Application**
   ```bash
   python main.py
   ```
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📖 How to Use
1. **Enter Job Description**: Paste the job requirements into the text area.
2. **Upload Resumes**: Select multiple resume files (PDF, DOCX, or TXT).
3. **Match**: Click the "Match Resumes" button.
4. **Results**: View the ranked list of candidates with their calculated similarity scores.

## 🧠 How it Works
1. **Text Extraction**: The system parses various file formats into raw text.
2. **Vectorization**: It converts the text into numerical vectors using the **TF-IDF** (Term Frequency-Inverse Document Frequency) method.
3. **Similarity Calculation**: It calculates the **Cosine Similarity** between the job description vector and each resume vector.
4. **Ranking**: Results are sorted, and the top candidates are presented to the user.

---
*Developed as part of an NLP Project to streamline the recruitment process.*
