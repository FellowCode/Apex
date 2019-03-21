from django.core.mail import EmailMultiAlternatives

admin_emails = ['sergo79_f1@mail.ru', 'pipiecvk@mail.ru', 'support@apex79.ru']

def send_servorder_mail(user_mail, order_id):
    subject, from_email = 'Заказ принят', 'info@apex79.ru'
    text_content = 'Ваш заказ #' + str(order_id) + ' принят.\n'
    text_content += 'Мы свяжемся с вами для уточнения заказа.\n'
    text_content += 'Если вы получили письмо по ошибке, вы можете его проигнорировать.\n'
    text_content += 'Задать вопрос можно на почту: support@apex79.ru\n'
    text_content += 'Телефон для справок: 89841284264'

    html_content = '<p>Ваш заказ #' + str(order_id) + ' принят.</p>'
    html_content += '<p>Мы свяжемся с вами для уточнения заказа</p>'
    html_content += '<p>Если вы получили письмо по ошибке, вы можете его проигнорировать.</p>'
    html_content += '<p>Задать вопрос можно на почту: <b>support@apex79.ru</b></p>'
    html_content += '<p>Телефон для справок: <b>89841284264</b></p>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, [user_mail])
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)

    subject, from_email = 'Поступил заказ', 'info@apex79.ru'
    text_content = 'Поступил заказ ' + str(order_id) + '\n'
    text_content += 'Подробные данные заказа: http://apex79.ru/admin/Service/serviceorder/' + str(order_id) + '/change/\n'
    text_content += 'Список заказов: http://apex79.ru/admin/Service/serviceorder/\n'

    html_content = '<p>Поступил заказ <b>' + str(order_id) + '</b></p>'
    html_content += '<p>Подробные данные заказа: http://apex79.ru/admin/Service/serviceorder/' + str(order_id) + '/change/</p>'
    html_content += '<p>Список заказов: http://apex79.ru/admin/Service/serviceorder/</p>'

    msg = EmailMultiAlternatives(subject, text_content, from_email, admin_emails)
    msg.attach_alternative(html_content, "text/html")
    msg.send(fail_silently=False)
