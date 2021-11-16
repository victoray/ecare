from rest_framework import viewsets, permissions

from ecare.service.models import Service, ServiceAddress, Appointment
from ecare.service.serializers import (
    ServiceSerializer,
    ServiceAddressSerializer,
    AppointmentSerializer,
)


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        user = self.request.user
        queryset = Service.objects.all()
        username = self.request.query_params.get("user")
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset


class ServiceAddressViewSet(viewsets.ModelViewSet):
    queryset = ServiceAddress.objects.all()
    serializer_class = ServiceAddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
