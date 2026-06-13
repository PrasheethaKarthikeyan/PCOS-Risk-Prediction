from flask import Flask, render_template, request
import pickle
import pandas as pd

app = Flask(__name__)

model = pickle.load(open("../model/pcos_model.pkl", "rb"))

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/predict", methods=["POST"])
def predict():

    features = [
        float(request.form["age"]),
        float(request.form["weight"]),
        float(request.form["height"]),
        float(request.form["bmi"]),
        float(request.form["pulse"])
    ]

    prediction = model.predict([features])

    result = "PCOS Risk Detected" if prediction[0] == 1 else "Low PCOS Risk"

    return render_template("index.html", prediction=result)

if __name__ == "__main__":
    app.run(debug=True)