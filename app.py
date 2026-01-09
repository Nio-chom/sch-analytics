from flask import Flask, render_template, request, redirect, url_for
import os

app = Flask(__name__)
results = []

@app.route("/", methods=["GET", "POST"])
def index():
    if request.method == "POST":
        name = request.form.get("name", "Аноним")
        gender = request.form.get("gender", "male")
        answer = int(request.form.get("study_habit", 3))
        results.append({"name": name, "gender": gender, "answer": answer})
        return redirect("/results")
    return render_template("index.html")

@app.route("/results")
def show_results():
    males = [r["answer"] for r in results if r["gender"] == "male"]
    females = [r["answer"] for r in results if r["gender"] == "female"]
    male_avg = round(sum(males)/len(males), 2) if males else 0
    female_avg = round(sum(females)/len(females), 2) if females else 0
    return render_template("results.html", male_avg=male_avg, female_avg=female_avg)

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 5000))
    app.run(host="0.0.0.0", port=port)
