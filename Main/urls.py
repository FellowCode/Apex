from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('serviceorder/accept/', service_order_accept),
    path('serviceorder/', service_order),
]