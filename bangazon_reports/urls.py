from django.urls import path
from .views import ProductList, InexpensiveProductList

urlpatterns = [
    path('reports/expensiveproducts', ProductList.as_view()),
    path('reports/inexpensiveproducts', InexpensiveProductList.as_view()),
]
