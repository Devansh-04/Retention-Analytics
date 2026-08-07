SELECT
    customer_segment,
    COUNT(DISTINCT customer_id) AS customer_count,
    ROUND(AVG(purchase_amount),2) AS avg_purchase_amount,
    ROUND(AVG(previous_purchases),2) AS avg_previous_purchases,
    ROUND(AVG(promo_dependency_score),3) AS avg_promo_dependency,
    ROUND(AVG(review_rating),2) AS avg_review_rating,
    ROUND(AVG(retention_score),3) AS avg_retention_score
FROM final_customer_segments
GROUP BY customer_segment
ORDER BY avg_retention_score DESC;