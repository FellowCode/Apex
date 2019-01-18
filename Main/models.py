from django.db import models


class ServiceOrder(models.Model):
    service_type = models.CharField(max_length=64, default='')
    email = models.EmailField()
    name = models.CharField(max_length=128)
    phone = models.CharField(max_length=11)
    note = models.TextField()

    def __str__(self):
        return str(self.service_type) + ' ' + str(self.email)
