import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score
import pickle

df = pd.read_csv("dataset/PCOS_data.csv")

df.columns = df.columns.str.strip()

df.drop("Unnamed: 44", axis=1, inplace=True)

# Clean problematic columns
for col in df.columns:
    df[col] = pd.to_numeric(df[col], errors="coerce")

df.fillna(df.mean(numeric_only=True), inplace=True)

# Only 5 features
X = df[
    [
        "Age (yrs)",
        "Weight (Kg)",
        "Height(Cm)",
        "BMI",
        "Pulse rate(bpm)"
    ]
]

y = df["PCOS (Y/N)"]

X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

model = RandomForestClassifier(
    n_estimators=200,
    random_state=42
)

model.fit(X_train, y_train)

pred = model.predict(X_test)

print("Accuracy:", accuracy_score(y_test, pred))

pickle.dump(model, open("model/pcos_model.pkl", "wb"))

print("Model Saved Successfully!")