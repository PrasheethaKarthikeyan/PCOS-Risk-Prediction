# PCOS Risk Prediction Using Machine Learning

## Project Overview

Polycystic Ovary Syndrome (PCOS) is one of the most common hormonal disorders affecting women. Early detection of PCOS can help in timely treatment and lifestyle management.

This project uses Machine Learning to predict the risk of PCOS based on various health parameters. A Random Forest Classifier is trained on a PCOS dataset and deployed as a web application using Flask and Render.

---

## Features

* Predicts PCOS risk using Machine Learning
* User-friendly web interface
* Trained using Random Forest Classifier
* Real-time prediction
* Cloud deployment using Render
* Open-source project hosted on GitHub

---

## Technology Stack

### Frontend

* HTML
* CSS

### Backend

* Flask (Python)

### Machine Learning

* Scikit-Learn
* Pandas
* NumPy

### Deployment

* GitHub
* Render

---

## Dataset

The dataset contains medical and clinical information related to PCOS, including:

* Age
* Weight
* Height
* BMI
* Pulse Rate
* Blood Test Parameters
* Hormonal Measurements
* Follicle Information
* Other Health Indicators

Target Variable:

* PCOS (Y/N)

  * 1 = PCOS Detected
  * 0 = No PCOS

---

## Machine Learning Model

Algorithm Used:

* Random Forest Classifier

Steps Performed:

1. Data Collection
2. Data Cleaning
3. Missing Value Handling
4. Feature Selection
5. Train-Test Split
6. Model Training
7. Model Evaluation
8. Model Deployment

Model Accuracy:

**85.32%**

---

## Project Structure

```text
PCOS-Risk-Prediction/
│
├── app/
│   ├── app.py
│   └── templates/
│       └── index.html
│
├── dataset/
│   └── PCOS_data.csv
│
├── model/
│   └── pcos_model.pkl
│
├── train_model.py
├── requirements.txt
├── Procfile
└── README.md
```

---

## Installation

Clone the repository:

```bash
git clone https://github.com/PrasheethaKarthikeyan/PCOS-Risk-Prediction.git
```

Move to project directory:

```bash
cd PCOS-Risk-Prediction
```

Install dependencies:

```bash
pip install -r requirements.txt
```

Run the application:

```bash
python app/app.py
```

Open:

```text
http://127.0.0.1:5000
```

---

## Deployment

The application is deployed using Render.

Live Application:

https://pcos-risk-prediction.onrender.com

---

## Sample Input

* Age: 25
* Weight: 65
* Height: 160
* BMI: 25
* Pulse Rate: 78

---

## Future Enhancements

* Probability-based risk prediction
* Interactive dashboard
* Data visualization
* Multiple ML model comparison
* User authentication
* Mobile-friendly UI

---

## Conclusion

This project demonstrates the application of Machine Learning in healthcare by predicting the risk of PCOS. It provides a simple and effective solution for early risk assessment and showcases the complete ML pipeline from data preprocessing to cloud deployment.

---

## Author

**Prasheetha K**

B.E. Computer Science and Engineering(Artificial Intelligence and Machine Learning)
