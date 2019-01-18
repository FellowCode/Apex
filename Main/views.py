from django.shortcuts import render
from .models import *
from Apex.helper import checkReCaptcha
from .helper import *


def index(request):
    return render(request, 'Main/Index.html')


def service_order(request):
    if request.method == 'GET':
        service_id = '1'
        try:
            service_id = request.GET['id']
        except: pass
        service_type_verbose = get_service_verbose_name(service_id)
        return render(request, 'Main/ServiceOrder.html', {'service_id': service_id,
                                                          'service_type_verbose': service_type_verbose})

def service_order_accept(request):
    if request.method == 'POST':
        if checkReCaptcha(request.POST['g-recaptcha-response']):
            service_verbose_name = get_service_verbose_name(request.POST['service_id'])
            order = ServiceOrder(service_type=service_verbose_name, name=request.POST['name'],
                                                email=request.POST['email'], phone=request.POST['phone'],
                                                note=request.POST['note'])
            order.save()
            return render(request, 'Main/SupportAccept.html')
