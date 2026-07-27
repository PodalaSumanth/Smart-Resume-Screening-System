from flask import Flask, render_template, request
import os
from resume_parser import extract_text
from model import calculate_score

app = Flask(__name__)
UPLOAD_FOLDER = "uploads"
app.config["UPLOAD_FOLDER"] = UPLOAD_FOLDER

@app.route("/", methods=["GET", "POST"])
def home():

    score = None
    recommendation = ""
    resume_preview = ""
    matched_skills = []
    missing_skills = []
    suggestions = ""

    if request.method == "POST":

        file = request.files["resume"]
        job_description = request.form["job_description"]
        if file:
            file_path = os.path.join(app.config["UPLOAD_FOLDER"], file.filename)
            file.save(file_path)
            resume_text = extract_text(file_path)
            resume_preview = resume_text[:500]
            score, matched_skills, missing_skills = calculate_score(resume_text, job_description)
            suggestions = []
            missing = [skill.lower() for skill in missing_skills]
            if "html" in missing:
                suggestions.append("👉 Add HTML to improve your frontend skills.")

            if "css" in missing:
                suggestions.append("👉 Add CSS for better web design skills.")

            if "javascript" in missing:
                suggestions.append("👉 Improve JavaScript for interactive websites.")

            if "sql" in missing:
                suggestions.append("👉 Practice SQL for database management.")

            if "git" in missing:
                suggestions.append("👉 Learn Git and GitHub for version control.")
            if score >= 80:
                recommendation = "🟢 Excellent Match"
            elif score >=60:
                recommendation = "🟡 Good Match"
            else:
                recommendation = "🔴 Needs Improvement"
            print(suggestions)
    return render_template("index.html", score=score, recommendation=recommendation, resume_preview=resume_preview, matched_skills=matched_skills, missing_skills=missing_skills, suggestions=suggestions)

if __name__ == "__main__":
    app.run(debug=True)