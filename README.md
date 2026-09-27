# Insider Threat Detection System

A Python-based cybersecurity application that combines **machine learning anomaly detection** with a **rule-based risk scoring engine** to identify potentially suspicious insider activity.

The system uses an **Isolation Forest** model to detect anomalous employee behavior and combines the model output with security-related behavioral indicators to calculate a risk score from 0 to 100.

## Features

* Machine learning-based anomaly detection using Isolation Forest
* Preprocessing of categorical and numerical employee data
* Feature normalization using StandardScaler
* Rule-based risk scoring
* Detection of potentially high-risk employee activity
* Flask REST API
* `/high-risk` endpoint for retrieving high-risk records
* Included datasets for experimentation and analysis

## Technology Stack

* **Python**
* **Flask** – REST API
* **Pandas** – Data processing
* **NumPy** – Data generation and numerical operations
* **Scikit-learn** – Machine learning and preprocessing
* **Isolation Forest** – Anomaly detection

## Project Structure

```text
Insider_Threat_System/
│
├── app.py
├── model.py
├── preprocess.py
├── risk_engine.py
├── generate_data.py
│
├── data/
│   ├── insider_threat_clean_dataset.csv
│   └── user_activity.csv
│
└── README.md
```

> The `venv/` directory is a local Python virtual environment and should not be committed to GitHub.

## How It Works

The application follows these main steps:

```text
Dataset
   │
   ▼
Data Preprocessing
   │
   ├── Remove missing values
   ├── Encode categorical values
   └── Standardize features
   │
   ▼
Isolation Forest
   │
   ├── Anomaly Score
   └── Anomaly Label
   │
   ▼
Risk Engine
   │
   ├── Printing behavior
   ├── File burning activity
   ├── Late exit behavior
   ├── Weekend entry
   └── ML anomaly
   │
   ▼
Risk Score (0–100)
   │
   ▼
High-Risk API Results
```

## Machine Learning Model

The project uses the **Isolation Forest** algorithm from Scikit-learn.

The model is configured with:

* `contamination = 0.05`
* `random_state = 42`

The model identifies observations that differ significantly from normal behavior.

An observation is marked as an anomaly when the Isolation Forest prediction is `-1`.

## Risk Scoring

The project calculates a risk score based on several behavioral indicators.

| Indicator                   | Risk Points |
| --------------------------- | ----------: |
| More than 100 printed pages |         +20 |
| More than 10 files burned   |         +30 |
| Late exit                   |         +20 |
| Weekend entry               |         +20 |
| Machine learning anomaly    |         +50 |

The final score is capped at **100**.

Records with a risk score greater than **70** are returned by the high-risk endpoint.

## Dataset

The primary dataset is:

`data/insider_threat_clean_dataset.csv`

It contains **118,614 records** and **22 columns**, including features related to:

* Employee department
* Campus
* Position
* Seniority
* Contractor status
* Employee classification
* Foreign citizenship
* Criminal-record indicator
* Medical-history indicator
* Origin country
* Printing activity
* File-burning activity
* Travel/activity indicators
* Number of entries
* Campus activity
* Late exits
* Weekend entries
* Malicious activity label

The `is_malicious` column is excluded from the features used to train the anomaly-detection model.

### User Activity Dataset

The project also contains:

`data/user_activity.csv`

This dataset contains 1,000 generated activity records with:

* User
* Login hour
* Files accessed
* Data downloaded in MB

The dataset can be used for additional experimentation or future extensions of the system.

## Installation

Clone the repository:

```bash
git clone https://github.com/YOUR-USERNAME/Insider-Threat-System.git
cd Insider-Threat-System
```

Create a virtual environment:

```bash
python -m venv venv
```

Activate it on Windows:

```bash
venv\Scripts\activate
```

Install the required packages:

```bash
pip install flask pandas numpy scikit-learn
```

## Running the Application

Start the Flask application:

```bash
python app.py
```

The application runs in Flask's debug mode.

Open:

```text
http://127.0.0.1:5000/
```

The home endpoint returns:

```text
Insider Threat Detection Running
```

## API Endpoint

### Get High-Risk Records

```http
GET /high-risk
```

Example:

```text
http://127.0.0.1:5000/high-risk
```

The endpoint returns records whose calculated risk score is greater than 70 in JSON format.

## Data Generation

The `generate_data.py` script can generate synthetic user activity data.

Run:

```bash
python generate_data.py
```

It generates:

```text
data/user_activity.csv
```

The generated dataset contains simulated user login times, file-access activity, and downloaded data volumes.

## Future Improvements

Potential extensions include:

* Real-time user activity monitoring
* Dashboard for security analysts
* User-level risk history
* Visualization of anomaly scores
* Email or notification alerts for high-risk users
* Additional machine learning models
* Model evaluation using labeled malicious activity
* Integration with enterprise security logs
* Authentication and role-based access control
* Database integration for storing historical risk scores

## Disclaimer

This project is intended for **educational, research, and cybersecurity demonstration purposes**. Risk scores and anomaly detections should be reviewed in context and should not be treated as definitive evidence of malicious behavior.

## Author

Developed as a cybersecurity and machine learning project demonstrating insider-threat detection using anomaly detection and rule-based risk analysis.
