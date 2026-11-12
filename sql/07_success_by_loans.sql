-- Q7: Do customers with loans subscribe less?
SELECT housing AS has_housing_loan,
       loan AS has_personal_loan,
       COUNT(*) AS contacts,
       ROUND(100.0 * SUM(subscribed) / COUNT(*), 2) AS success_rate_pct
FROM bank_marketing
GROUP BY housing, loan
ORDER BY success_rate_pct DESC;