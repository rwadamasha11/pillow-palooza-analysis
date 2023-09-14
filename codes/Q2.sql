SELECT room_type, AVG (price)
FROM prices p 
LEFT JOIN room_types rt
ON p.listing_id = rt.listing_id
GROUP BY 1 
ORDER BY 2 DESC