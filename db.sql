SELECT u.id as customer_id, u.first_name || " " || u.last_name as full_name, s.name as store_name
FROM bangazon_api_favorite f
JOIN auth_user u 
ON f.customer_id = u.id
JOIN bangazon_api_store s 
ON f.store_id = s.id


