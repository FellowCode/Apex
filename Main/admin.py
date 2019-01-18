from django.contrib import admin
from .models import ServiceOrder

@admin.register(ServiceOrder)
class ServiceOrderAdmin(admin.ModelAdmin):
    readonly_fields = ['service_type', 'email', 'name', 'phone', 'note']
