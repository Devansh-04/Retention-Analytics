WITH segment_comparison AS (
    SELECT
        customer_segment,
        ml_customer_segment,
        COUNT(DISTINCT customer_id) AS customer_count,
        ROUND(AVG(purchase_amount),2) AS avg_purchase_amount,
        ROUND(AVG(previous_purchases),2) AS avg_previous_purchases,
        ROUND(AVG(promo_dependency_score),3) AS avg_promo_dependency,
        ROUND(AVG(value_score),3) AS avg_value_score
    FROM final_customer_segments
    GROUP BY
        customer_segment,
        ml_customer_segment
    HAVING COUNT(DISTINCT customer_id) >= 2
)
SELECT
    *,
    DENSE_RANK() OVER(
        ORDER BY customer_count DESC
    ) AS overlap_rank
FROM segment_comparison
ORDER BY overlap_rank;