from django.urls import path
from .views import ProductList

urlpatterns = [
    path('reports/expensiveproducts', ProductList.as_view()),
]
