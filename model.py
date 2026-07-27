from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

def calculate_score(resume_text, job_description):

    documents = [resume_text, job_description]

    vectorizer = TfidfVectorizer()
    vectors = vectorizer.fit_transform(documents)

    similarity = cosine_similarity(vectors[0:1], vectors[1:2])
    score = round(similarity[0][0] * 100, 2)

    skills = [
        "python", "java", "html", "css", "javascript",
        "sql", "flask", "django", "react", "git",
        "github", "machine learning", "data science",
        "power bi", "excel", "numpy", "pandas"
    ]

    resume_lower = resume_text.lower()
    job_lower = job_description.lower()

    matched_skills = []
    missing_skills = []

    for skill in skills:
        if skill in job_lower:
            if skill in resume_lower:
                matched_skills.append(skill.title())
            else:
                missing_skills.append(skill.title())

    return score, matched_skills, missing_skills