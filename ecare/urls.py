"""ecare URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from ecare.role.views import RoleViewSet
from ecare.service.views import (
    ServiceViewSet,
    ServiceAddressViewSet,
    AppointmentViewSet,
)
from ecare.user.views import UserViewSet

router = routers.DefaultRouter()
router.register(r"users", UserViewSet)
router.register(r"roles", RoleViewSet)
router.register(r"service_addresses", ServiceAddressViewSet)
router.register(r"services", ServiceViewSet, basename="service")
router.register(r"appointments", AppointmentViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("", include(router.urls)),
    path("api-auth/", include("rest_framework.urls", namespace="rest_framework")),
]
