from django.shortcuts import render
from .models import *
from Apex.helper import checkReCaptcha

def index(request):
    return render(request, 'Main/Index.html')


def service_order(request):
    if request.method == 'GET':
        service_type = 'pc'
        service_type_verbose = 'ПК'
        try:
            service_type = request.GET['type']
        except: pass
        return render(request, 'Main/ServiceOrder.html', {'service_type': service_type,
                                                          'service_type_verbose': service_type_verbose})

def service_order_accept(request):
    if request.method == 'POST':
        if checkReCaptcha(request.POST['response']):
            print(request.POST['type'])
            order = ServiceOrder(service_type=request.POST['type'], name=request.POST['name'],
                                                email=request.POST['email'], phone=request.POST['phone'],
                                                note=request.POST['note'])
            order.save()
            return render(request, 'Main/SupportAccept.html')
