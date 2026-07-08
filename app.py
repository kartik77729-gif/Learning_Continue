from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine

app = Flask(__name__)

Jobs = [
    {
        "id": 1,
        "title": "Data Analyst",
        "loaction": "Bengaluru, India",
        "salary": "Rs 10,00,000",
    },
    {
        "id": 1,
        "title": "Data Scientist",
        "loaction": "Mumbai, India",
    },
    {
        "id": 1,
        "title": "AI Engineer",
        "loaction": "Bengaluru, India",
        "salary": "Rs 14,00,000",
    },
    {
        "id": 1,
        "title": "Frontend Engineer",
        "loaction": "Remote",
        "salary": "Rs 8,00,000",
    },
    {
        "id": 1,
        "title": "Backend Engineer",
        "loaction": "Delhi, India",
        "salary": "Rs 17,00,000",
    },
]

def load_jobs_from_db():
    with engine.connect() as conn:
        result = conn.execute(text("SELECT * FROM jobs"))

@app.route("/")
def hello_world():
    return render_template("home.html", jobs=Jobs, company_name="Amazon AWS ")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
