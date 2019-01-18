def get_service_verbose_name(service_id):
    if service_id == '1':
        service_type_verbose = 'Выездная проверка автомобиля экспертом'
    elif service_id == '2':
        service_type_verbose = 'Эксперт на день'
    else:
        service_type_verbose = 'Подбор автомобиля под ключ'

    return service_type_verbose
