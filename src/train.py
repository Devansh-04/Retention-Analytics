import os
import joblib
import pandas as pd

from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATA_PATH = os.path.join(
    BASE_DIR,
    "data",
    "processed",
    "customer_features.csv"
)

ARTIFACT_DIR = os.path.join(
    BASE_DIR,
    "src",
    "artifacts"
)

os.makedirs(ARTIFACT_DIR, exist_ok=True)


df = pd.read_csv(DATA_PATH)


features = [
    "age",
    "purchase_amount",
    "review_rating",
    "previous_purchases",
    "frequency_score",
    "promo_dependency_score",
    "satisfaction_flag",
    "subscription_flag",
    "value_score",
    "retention_score"
]

X = df[features]


scaler = StandardScaler()
X_scaled = scaler.fit_transform(X)


kmeans = KMeans(
    n_clusters=5,
    random_state=42,
    n_init=10
)

kmeans.fit(X_scaled)


joblib.dump(
    scaler,
    os.path.join(ARTIFACT_DIR, "scaler.pkl")
)


joblib.dump(
    kmeans,
    os.path.join(ARTIFACT_DIR, "kmeans.pkl")
)


reference_data = {
    "purchase_amount": df["purchase_amount"].values,
    "previous_purchases": df["previous_purchases"].values,
    "frequency_score": df["frequency_score"].values
}

joblib.dump(
    reference_data,
    os.path.join(ARTIFACT_DIR, "reference_data.pkl")
)


print("Model training completed.")
print("Artifacts saved to:", ARTIFACT_DIR)