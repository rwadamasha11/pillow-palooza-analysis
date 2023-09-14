WITH t1 AS 
(
SELECT  borough, price * booked_days_365 as revenue  
FROM prices p 
LEFT JOIN reviews r
ON p.listing_id = r.listing_id
)
SELECT borough, SUM (revenue) AS est_revenue
FROM t1 
GROUP BY 1 