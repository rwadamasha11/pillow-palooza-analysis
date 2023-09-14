SELECT CORR(price, booked_days_365) AS correlation
FROM prices p 
LEFT JOIN reviews r
ON p.listing_id = r.listing_id