SELECT borough ,MIN (price) AS min_price, MAX (price) AS max_price, AVG (price) AS avg_price
FROM prices 
GROUP BY 1
ORDER BY 4,3,2 DESC