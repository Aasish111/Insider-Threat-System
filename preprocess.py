import pandas as pd
from sklearn.preprocessing import LabelEncoder, StandardScaler

def load_and_preprocess():

    # Load dataset
    df = pd.read_csv("data/insider_threat_clean_dataset.csv")

    print(df.columns)

    # Remove missing values
    df = df.dropna()

    # Convert categorical columns into numbers
    categorical_cols = df.select_dtypes(include=["object"]).columns

    le = LabelEncoder()

    for col in categorical_cols:
        df[col] = le.fit_transform(df[col])

    # Remove target column if present
    if "is_malicious" in df.columns:
        features = df.drop("is_malicious", axis=1)
    else:
        features = df.copy()

    # Normalize data
    scaler = StandardScaler()
    scaled_data = scaler.fit_transform(features)

    return df, scaled_data