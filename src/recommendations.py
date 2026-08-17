SEGMENT_INSIGHTS = {
    "Champions": {
        "retention_level": "High",
        "recommendation": "Prioritize loyalty benefits and personalized offers."
    },

    "Stable Mid-Value Customers": {
        "retention_level": "Medium-High",
        "recommendation": "Encourage repeat purchases through personalized recommendations."
    },

    "Promo-Dependent Regulars": {
        "retention_level": "Medium",
        "recommendation": "Use targeted promotions while monitoring discount dependency."
    },

    "One-Time Bargain Hunters": {
        "retention_level": "Low",
        "recommendation": "Use targeted follow-up campaigns to encourage a second purchase."
    },

    "At-Risk Low Value Customers": {
        "retention_level": "Low",
        "recommendation": "Use low-cost re-engagement campaigns and avoid excessive discounts."
    }
}


def get_segment_insight(segment):
    return SEGMENT_INSIGHTS.get(
        segment,
        {
            "retention_level": "Unknown",
            "recommendation": "No recommendation available."
        }
    )