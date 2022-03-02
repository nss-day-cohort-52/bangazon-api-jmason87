from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all

class CompletedOrdersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
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
            """)
            dataset = dict_fetch_all(db_cursor)
            completed_orders = []
            for row in dataset:
                order = {
                    "order_id": row['order_id'],
                    "name": row['full_name'],
                    "payment_type": row['payment_type'],
                    "total": row['total_price']
                }
                completed_orders.append(order)

        template = 'orders/completed_orders.html'
        
        # The context will be a dictionary that the template can access to show data
        context = {
            "completed_orders": completed_orders
        }

        return render(request, template, context)           