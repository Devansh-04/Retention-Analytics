SELECT
    value_tier,
    COUNT(DISTINCT customer_id) AS customer_count,
    ROUND(AVG(purchase_amount),2) AS avg_purchase_amount,
    ROUND(AVG(previous_purchases),2) AS avg_previous_purchases,
    ROUND(AVG(value_score),3) AS avg_value_score,
    ROUND(SUM(purchase_amount),0) AS total_revenue
FROM final_customer_segments
GROUP BY value_tier
ORDER BY
 CASE value_tier
    WHEN 'Premium Value' THEN 1
    WHEN 'High Value' THEN 2
    WHEN 'Mid Value' THEN 3
    WHEN 'Low Value' THEN 4
END;