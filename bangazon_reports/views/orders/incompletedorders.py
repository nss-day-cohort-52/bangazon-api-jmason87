from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all

# This class will need to be imported in the views/__init__.py
class IncompletedOrdersList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            # This is the SQL statement that will get the relevant data for report
            db_cursor.execute("""
            SELECT o.id as order_id, u.first_name || " " || u.last_name as full_name, sum(price) as total_price, pt.merchant_name as payment_type, o.created_on as created_on
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
            """)
            
            # This turns the fetch_all response into a dictionary
            dataset = dict_fetch_all(db_cursor)
            
            # This will be the list that holds the the data we get from the dataset
            incompleted_orders = []
            
            # This takes the dictionaries coming from dataset, and tells it what rows
            for row in dataset:
                # The keys defined here is what we'll use on the html side when interpolating
                # The values for each key are coming from the sql statement above (ex. SUM(price) as total_price)
                order = {
                    "order_id": row['order_id'],
                    "name": row['full_name'],
                    "total": row['total_price'],
                    "created_on": row['created_on']
                }
                # pushes the order to the incompleted_orders list
                incompleted_orders.append(order)
        
        #this is what file path we're using for the html 
        template = 'orders/incompleted_orders.html'
        
        # The context will be a dictionary that the template can access to show data
        # the key is what we'll use in the .html to iterate through for the data
        # the value, in this case is the incompleted_orders list from above
        context = {
            "incompleted_orders": incompleted_orders
        }

        return render(request, template, context)           