-- Q1: What is the overall subscription rate?
SELECT COUNT(*) AS total_contacts,
       SUM(subscribed) AS subscribers,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing;