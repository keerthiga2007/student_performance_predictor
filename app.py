from flask import Flask, render_template, request
from main import model
import pandas as pd

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def home():
    prediction = ""  # Default empty prediction for initial GET request
    
    if request.method == "POST":
        # 1. Get form values & cast to float
        study_hours = float(request.form["studyhours"])
        attendance = float(request.form["attendance"])
        
        # 2. Create DataFrame (MUST be inside POST block)
        new_student = pd.DataFrame({
            "StudyHours": [study_hours],
            "Attendance": [attendance]
        })
        
        # 3. Make prediction (MUST be inside POST block)
        result = model.predict(new_student)
        
        if result[0] == 1:
            prediction = "Pass"
        else:
            prediction = "Fail"

    # 4. Return template at the end
    return render_template("index.html", prediction=prediction)

if __name__ == "__main__":
    app.run(debug=True)