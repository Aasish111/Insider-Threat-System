from flask import Flask, jsonify

from preprocess import load_and_preprocess
from model import train_model, predict
from risk_engine import compute_risk

app = Flask(__name__)

# Load data
df, scaled_data = load_and_preprocess()

# Train model
model = train_model(scaled_data)

# Predict anomalies
scores, labels = predict(model, scaled_data)

df["anomaly_score"] = scores
df["anomaly"] = labels

# Risk score
df["risk_score"] = df.apply(compute_risk, axis=1)


@app.route("/")
def home():
    return "Insider Threat Detection Running"


@app.route("/high-risk")
def high_risk():
    return jsonify(df[df["risk_score"] > 70].to_dict(orient="records"))


if __name__ == "__main__":
    app.run(debug=True)