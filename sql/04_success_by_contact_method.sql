-- Q4: Does the contact method matter?
SELECT contact,
       COUNT(*) AS contacts,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing
GROUP BY contact
ORDER BY success_rate_pct DESC;
