from django.urls import path
from .views import *

urlpatterns = [
    path('', index),
    path('serviceorder/result/', service_order_create),
    path('serviceorder/', service_order),
    path('test/', test),
]