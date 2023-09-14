SELECT neighbourhood , room_type , AVG (price_per_month)
FROM prices p 
LEFT JOIN room_types rt
ON p.listing_id = rt.listing_id
GROUP BY 1,2
