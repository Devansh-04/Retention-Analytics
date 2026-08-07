WITH location_summary AS (
    SELECT
        location,
        COUNT(DISTINCT customer_id) AS customer_count,
        SUM(purchase_amount) AS total_revenue,
        AVG(purchase_amount) AS avg_purchase_amount,
        AVG(previous_purchases) AS avg_previous_purchases,
        AVG(promo_dependency_score) AS avg_promo_dependency,
        AVG(retention_score) AS avg_retention_score
    FROM final_customer_segments
    GROUP BY location
)

SELECT
    location,
    customer_count,
    ROUND(total_revenue,0) AS total_revenue,
    ROUND(avg_purchase_amount,2) AS avg_purchase_amount,
    ROUND(avg_previous_purchases,2) AS avg_previous_purchases,
    ROUND(avg_promo_dependency,3) AS avg_promo_dependency,
    ROUND(avg_retention_score,3) AS avg_retention_score
FROM location_summary
ORDER BY avg_purchase_amount DESC;