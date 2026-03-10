from flask import Flask,render_template,request
import pickle
import numpy as np

app = Flask(__name__)

model = pickle.load(open("model.pkl","rb"))
gender_encoder = pickle.load(open("gender.pkl","rb"))
edu_encoder = pickle.load(open("edu.pkl","rb"))
job_encoder = pickle.load(open("job.pkl","rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict",methods=["POST"])
def predict():

    age = float(request.form["age"])
    gender = request.form["gender"]
    education = request.form["education"]
    job = request.form["job"]
    experience = float(request.form["experience"])

    gender = gender_encoder.transform([gender])[0]
    education = edu_encoder.transform([education])[0]

    try:
        job = job_encoder.transform([job])[0]
    except:
        job = 0

    prediction = model.predict([[age,gender,education,job,experience]])

    salary = round(prediction[0],2)

    return render_template(
        "index.html",
        prediction_text=f"Estimated Salary : ₹ {salary}"
    )

if __name__ == "__main__":
    app.run(debug=True)