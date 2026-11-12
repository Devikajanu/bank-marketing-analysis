-- Q2: Which job types subscribe the most?
SELECT job,
       COUNT(*) AS contacts,
       SUM(subscribed) AS subscribers,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing
GROUP BY job
ORDER BY success_rate_pct DESC;