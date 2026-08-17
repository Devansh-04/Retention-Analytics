import numpy as np
import pandas as pd


FREQUENCY_MAP = {
    "Weekly": 7,
    "Fortnightly": 6,
    "Monthly": 5,
    "Quarterly": 4,
    "Every 3 Months": 4,
    "Annually": 2,
    "Bi-Weekly": 1
}


def percentile_rank(value, reference_values):
    """
    Approximate the percentile rank of a new value
    using the training dataset.
    """
    reference_values = np.asarray(reference_values)

    return np.searchsorted(
        np.sort(reference_values),
        value,
        side="right"
    ) / len(reference_values)


def create_features(customer, reference_data):
    """
    Convert raw customer information into the same
    features used by the clustering model.
    """

    purchase_amount = customer["purchase_amount"]
    previous_purchases = customer["previous_purchases"]
    review_rating = customer["review_rating"]
    frequency = customer["frequency_of_purchases"]

    discount_applied = customer["discount_applied"]
    promo_code_used = customer["promo_code_used"]
    subscription_status = customer["subscription_status"]

    discount_flag = 1 if discount_applied == "Yes" else 0
    promo_flag = 1 if promo_code_used == "Yes" else 0
    subscription_flag = 1 if subscription_status == "Yes" else 0

    frequency_score = FREQUENCY_MAP.get(frequency, 4)

    satisfaction_flag = 1 if review_rating >= 4.0 else 0

    promo_dependency_score = (
        discount_flag + promo_flag
    ) / 2

    purchase_rank = percentile_rank(
        purchase_amount,
        reference_data["purchase_amount"]
    )

    previous_purchase_rank = percentile_rank(
        previous_purchases,
        reference_data["previous_purchases"]
    )

    frequency_rank = percentile_rank(
        frequency_score,
        reference_data["frequency_score"]
    )

    value_score = (
        0.30 * purchase_rank +
        0.25 * previous_purchase_rank +
        0.20 * frequency_rank +
        0.10 * subscription_flag +
        0.10 * satisfaction_flag -
        0.05 * promo_dependency_score
    )

    retention_score = (
        0.6 * previous_purchase_rank +
        0.4 * frequency_rank
    )

    features = pd.DataFrame([{
        "age": customer["age"],
        "purchase_amount": purchase_amount,
        "review_rating": review_rating,
        "previous_purchases": previous_purchases,
        "frequency_score": frequency_score,
        "promo_dependency_score": promo_dependency_score,
        "satisfaction_flag": satisfaction_flag,
        "subscription_flag": subscription_flag,
        "value_score": value_score,
        "retention_score": retention_score
    }])

    return features