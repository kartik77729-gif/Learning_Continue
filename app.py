from flask import Flask, render_template, jsonify
from sqlalchemy import text
from database import engine

app = Flask(__name__)

@app.route("/")
def hello_world():
    def load_jobs_from_db():
        with engine.connect() as conn:
            result = conn.execute(text("SELECT * FROM jobs"))
            jobs = [row._asdict() for row in result.all()]
            return jobs
        return render_template("home.html", jobs, company_name="Amazon AWS ")


@app.route("/api/jobs")
def list_jobs():
    return jsonify(Jobs)


if __name__ == "__main__":
    app.run(host="0.0.0.0", debug=True)
