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


SELECT o.id order_id, u.first_name, u.last_name, pt.merchant_name payment_type, op.*, SUM(p.price) total_price
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
