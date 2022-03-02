from django.urls import path
from .views import ProductList, InexpensiveProductList, CompletedOrdersList

urlpatterns = [
    path('reports/expensiveproducts', ProductList.as_view()),
    path('reports/inexpensiveproducts', InexpensiveProductList.as_view()),
    path('orders/completedorders', CompletedOrdersList.as_view()),
]
