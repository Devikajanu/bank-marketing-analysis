-- Q6: Do customers who subscribed before subscribe again?
SELECT poutcome AS previous_outcome,
       COUNT(*) AS contacts,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing
GROUP BY poutcome
ORDER BY success_rate_pct DESC;