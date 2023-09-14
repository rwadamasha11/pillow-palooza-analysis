SELECT borough,room_type , COUNT(DISTINCT p.listing_id) AS listing_count
FROM prices p 
LEFT JOIN room_types rt
ON p.listing_id = rt.listing_id
GROUP BY 1,2
ORDER BY 3 DESC
