from django.contrib import admin

# Register your models here.
from ecare.service.models import Service, ServiceAddress, Appointment

admin.site.register(Service)
admin.site.register(ServiceAddress)
admin.site.register(Appointment)
