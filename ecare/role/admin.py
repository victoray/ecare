from django.contrib import admin

# Register your models here.
from ecare.role.models import Role


class RoleAdmin(admin.ModelAdmin):
    list_display = ("uuid", "name", "type")


admin.site.register(Role, RoleAdmin)
