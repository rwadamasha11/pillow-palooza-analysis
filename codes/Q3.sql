SELECT borough, AVG(price_per_month)
FROM prices 
GROUP BY 1
ORDER BY 2 DESC