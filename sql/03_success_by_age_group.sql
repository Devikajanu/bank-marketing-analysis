-- Q3: Which age groups subscribe the most?
SELECT age_group,
       COUNT(*) AS contacts,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing
GROUP BY age_group
ORDER BY success_rate_pct DESC;