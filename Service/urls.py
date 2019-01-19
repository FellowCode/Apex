from django.urls import path
from .views import *

urlpatterns = [
    path('order/result/', service_order_create),
    path('order/', service_order),
]