
SELECT category,
    COUNT(DISTINCT customer_id) AS customer_count,
    ROUND(AVG(purchase_amount),2) AS avg_purchase,
    ROUND(AVG(previous_purchases),2) AS avg_previous_purchases,
    ROUND(AVG(frequency_score),2) AS avg_purchase_frequency,
    ROUND(AVG(retention_score),3) AS avg_retention_rate,
    ROUND(AVG(promo_dependency_score),3) AS avg_promo_dependency
FROM final_customer_segments
GROUP BY category
ORDER BY customer_count DESC;