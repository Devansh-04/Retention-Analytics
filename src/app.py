import os
import joblib

from fastapi import FastAPI
from pydantic import BaseModel

from .preprocessing import create_features
from .recommendations import get_segment_insight


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

ARTIFACT_DIR = os.path.join(
    BASE_DIR,
    "src",
    "artifacts"
)


scaler = joblib.load(
    os.path.join(ARTIFACT_DIR, "scaler.pkl")
)

kmeans = joblib.load(
    os.path.join(ARTIFACT_DIR, "kmeans.pkl")
)

reference_data = joblib.load(
    os.path.join(ARTIFACT_DIR, "reference_data.pkl")
)


app = FastAPI(
    title="Customer Retention API",
    description="Customer segmentation and retention analysis API",
    version="1.0.0"
)


class CustomerInput(BaseModel):

    age: int

    purchase_amount: float

    review_rating: float

    previous_purchases: int

    frequency_of_purchases: str

    discount_applied: str

    promo_code_used: str

    subscription_status: str


cluster_name_map = {
    0: "Stable Mid-Value Customers",
    1: "Champions",
    2: "Promo-Dependent Regulars",
    3: "One-Time Bargain Hunters",
    4: "At-Risk Low Value Customers"
}


@app.get("/")
def home():

    return {
        "message": "Customer Retention API is running"
    }


@app.get("/health")
def health():

    return {
        "status": "healthy"
    }


@app.post("/predict")
def predict(customer: CustomerInput):

    customer_data = customer.model_dump()

    features = create_features(
        customer_data,
        reference_data
    )

    scaled_features = scaler.transform(features)

    cluster = int(
        kmeans.predict(scaled_features)[0]
    )

    segment = cluster_name_map.get(
        cluster,
        "Unknown Segment"
    )

    insight = get_segment_insight(segment)

    return {
    "cluster": cluster,
    "customer_segment": segment,
    "retention_level": insight["retention_level"],
    "recommendation": insight["recommendation"]
}