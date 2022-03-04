from django.shortcuts import render
from django.db import connection
from django.views import View

from bangazon_reports.views.helpers import dict_fetch_all

class FavoritesList(View):
    def get(self, request):
        with connection.cursor() as db_cursor:
            db_cursor.execute("""
            SELECT u.id as customer_id, u.first_name || " " || u.last_name as full_name, s.name as store_name
            FROM bangazon_api_favorite f
            JOIN auth_user u 
            ON f.customer_id = u.id
            JOIN bangazon_api_store s 
            ON f.store_id = s.id
            """)
            dataset = dict_fetch_all(db_cursor)
            list_of_user_favorites = []
            for row in dataset:
                
                store = {
                    'store': row['store_name']
                }

                # This code is equivalent to:
                # customer_dict = None
                # for customer_store in list_of_user_favorties :
                #     if customer_store['customer_id'] == row['customer_id']:
                #         customer_dict = customer_store
                customer_dict = next(
                    (
                        customer_store for customer_store in list_of_user_favorites
                        if customer_store['customer_id'] == row['customer_id']
                    ),
                    None
                )
                
                if customer_dict:
                # If the customer_dict is already in the list_of_user_favorites list, append the store to the customer list
                    customer_dict['store'].append(store)
                else:
                    # If the customer is not on the list_of_user_favorites list, create and add the customer to the list
                    list_of_user_favorites.append({
                        'customer_id': row['customer_id'],
                        'name': row['full_name'],
                        'store': [store]
                    })
                            
        template = "favorites/userfavorites.html"
        context = {
            "favorites_list": list_of_user_favorites
        }
        return render(request, template, context)                 
