from django.urls import path
from .views import *

urlpatterns = [
path('products/', ProductList.as_view(), name='products'),
path('orders/', SummaryOrder.as_view(), name='orders'),
path('addorder/', ProductOrder.as_view(),name='addorder'),

 ]