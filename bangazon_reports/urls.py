from django.urls import path

from .views import ProductList, InexpensiveProductList, CompletedOrdersList, IncompletedOrdersList, FavoritesList

urlpatterns = [
    # this defines the URL we'll use to to see the report and the views needed to get the relevant data
    path('reports/expensiveproducts', ProductList.as_view()),
    path('reports/inexpensiveproducts', InexpensiveProductList.as_view()),
    path('orders/completedorders', CompletedOrdersList.as_view()),
    path('orders/incompletedorders', IncompletedOrdersList.as_view()),
    path('favorites/userfavorites', FavoritesList.as_view()),

]
