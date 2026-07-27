# Smart Resume Screening System

## 📌 Overview
The Smart Resume Screening System is a Flask-based web application that analyzes a candidate's resume against a job description. It calculates a similarity score using TF-IDF and Cosine Similarity, identifies matched and missing skills, and provides resume improvement suggestions.

## ✨ Features
- Upload resume in PDF format
- Enter a job description
- Resume match score
- Matched skills
- Missing skills
- Resume improvement suggestions
- Resume preview
- Recommendation (Excellent Match / Good Match / Needs Improvement)

## 🛠️ Technologies Used
- Python
- Flask
- HTML
- CSS
- Scikit-learn
- PyPDF2 (or your PDF library)

## 📂 Project Structure
```
smart_resume_screening_system/
│── app.py
│── model.py
│── resume_parser.py
│── requirements.txt
│── templates/
│   └── index.html
│── static/
│   └── style.css
│── uploads/
```

## 🚀 Installation

1. Clone the repository:
```bash
git clone https://github.com/your-username/Smart-Resume-Screening-System.git
```

2. Move into the project folder:
```bash
cd Smart-Resume-Screening-System
```

3. Install dependencies:
```bash
pip install -r requirements.txt
```

4. Run the application:
```bash
python app.py
```

5. Open your browser and visit:
```
http://127.0.0.1:5000
```



## 🔮 Future Improvements
- DOCX resume support
- AI-based resume feedback
- ATS score analysis
- User login system
- Cloud deployment

## 👨‍💻 Author

**Podala Sumanth**

- B.Tech in Artificial Intelligence and Data Science
- Python | Flask | Machine Learning

## 📄 License

This project is created for learning and educational purposes.
