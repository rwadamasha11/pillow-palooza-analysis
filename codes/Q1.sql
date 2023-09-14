SELECT room_type,COUNT (room_type) 
FROM room_types 
GROUP BY 1 
ORDER BY 2 DESC