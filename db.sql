SELECT o.id order_id, u.first_name || " " || u.last_name as full_name, pt.merchant_name payment_type, SUM(p.price) total_price
FROM bangazon_api_order o
JOIN auth_user u
ON o.user_id = u.id
JOIN bangazon_api_paymenttype pt 
ON o.payment_type_id = pt.id
JOIN bangazon_api_orderproduct op 
ON o.id = op.order_id
JOIN bangazon_api_product p 
ON op.product_id = p.id
GROUP BY o.id


SELECT o.id as order_id, u.first_name || " " || u.last_name as full_name, sum(price) as total_paid, pt.merchant_name as payment_type, o.created_on
FROM bangazon_api_order o
JOIN auth_user u
ON o.user_id = u.id
LEFT JOIN bangazon_api_paymenttype pt 
ON pt.id = o.payment_type_id
JOIN bangazon_api_orderproduct op 
ON op.order_id = o.id
JOIN bangazon_api_product p 
ON p.id = op.product_id
WHERE payment_type is NULL
GROUP BY order_id
ORDER BY o.created_on ASC



