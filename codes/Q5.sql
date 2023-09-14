SELECT room_type ,COUNT (room_type) AS count_rooms
FROM prices p 
LEFT JOIN room_types rt
ON p.listing_id = rt.listing_id
WHERE price > 500
GROUP BY 1
ORDER BY 2 DESC
