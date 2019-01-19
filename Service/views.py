from Apex.helper import checkReCaptcha
from django.shortcuts import render
from .helper import get_service_verbose_name
from SMTP.tasks import send_servorder_mail
from .models import ServiceOrder

def service_order(request):
    if request.method == 'GET':
        service_id = '1'
        try:
            service_id = request.GET['id']
        except: pass
        service_type_verbose = get_service_verbose_name(service_id)
        return render(request, 'Service/ServiceOrder.html', {'service_id': service_id,
                                                          'service_type_verbose': service_type_verbose})
    else:
        return render(request, 'Main/Index.html')

def service_order_create(request):
    if request.method == 'POST':
        if checkReCaptcha(request.POST['g-recaptcha-response']):
            service_verbose_name = get_service_verbose_name(request.POST['service_id'])
            email = request.POST['email']
            order = ServiceOrder(service_type=service_verbose_name, name=request.POST['name'],
                                 email=email, phone=request.POST['phone'],
                                 note=request.POST['note'])
            order.save()
            try:
                send_servorder_mail(email, order.id)
                return render(request, 'Service/OrderAccept.html')
            except:
                order.delete()
                return render(request, 'Service/OrderError.html')
        else:
            return render(request, 'Main/Index.html')
    else:
        return render(request, 'Main/Index.html')
