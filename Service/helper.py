def get_service_verbose_name(service_id):
    if service_id == '1':
        service_type_verbose = 'Выездная проверка автомобиля экспертом'
    elif service_id == '2':
        service_type_verbose = 'Эксперт на день'
    elif service_id == '3':
        service_type_verbose = 'Подбор автомобиля под ключ'
    else:
        service_type_verbose = 'Укажите услугу в примечании'

    return service_type_verbose