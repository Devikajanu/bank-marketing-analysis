-- Q5: Which months have the best success rate?
SELECT month,
       COUNT(*) AS contacts,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing
GROUP BY month
ORDER BY success_rate_pct DESC;