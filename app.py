from flask import Flask, render_template,request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""

    if request.method == "POST":
        study_hours = request.form["studyhours"]
        attendance = request.form["attendance"]

        prediction = f"Study Hours: {study_hours}, Attendance: {attendance}"

    return render_template("index.html", prediction=prediction)

    return render_template("index.html")

if __name__ == "__main__":
    app.run(debug=True)