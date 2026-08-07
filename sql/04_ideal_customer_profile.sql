WITH customer_profiles AS (
    SELECT
        age_group,
        gender,
        category,
        payment_method,
        shipping_type,
        frequency_of_purchases,
        COUNT(DISTINCT customer_id) AS customer_count,
        ROUND(AVG(purchase_amount),2) AS avg_purchase_amount,
        ROUND(AVG(previous_purchases),2) AS avg_previous_purchases,
        ROUND(AVG(review_rating),2) AS avg_review_rating,
        ROUND(AVG(promo_dependency_score),3) AS avg_promo_dependency,
        ROUND(AVG(value_score),3) AS avg_value_score,
        ROUND(AVG(retention_score),3) AS avg_retention_score
    FROM final_customer_segments
    GROUP BY
        age_group,
        gender,
        category,
        payment_method,
        shipping_type,
        frequency_of_purchases
    HAVING COUNT(DISTINCT customer_id) >= 3
)

SELECT *,
       DENSE_RANK() OVER (
           ORDER BY avg_value_score DESC,
                    avg_retention_score DESC
       ) AS profile_rank
FROM customer_profiles
ORDER BY profile_rank;