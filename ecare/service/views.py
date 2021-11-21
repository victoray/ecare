from django_filters.rest_framework import DjangoFilterBackend
from geojson import Feature, Point
from rest_framework import viewsets, permissions, filters
from rest_framework.request import Request
from turfpy.measurement import points_within_polygon, boolean_point_in_polygon
from turfpy.transformation import circle

from ecare.service.models import Service, ServiceAddress, Appointment
from ecare.service.serializers import (
    ServiceSerializer,
    ServiceAddressSerializer,
    AppointmentSerializer,
)


class AddressFilterBackend(filters.BaseFilterBackend):
    def filter_queryset(self, request: Request, queryset, view):
        lng = request.query_params.get("longitude")
        lat = request.query_params.get("latitude")

        if lng and lat:
            center = Feature(geometry=Point((float(lng), float(lat))))
            cc = circle(center, radius=500, steps=10, units="km")
            matched_service = []
            services = Service.objects.all()
            for service in services:
                addresses: list[ServiceAddress] = service.addresses.all()
                for address in addresses:
                    point = Feature(
                        geometry=Point(
                            (float(address.longitude), float(address.latitude))
                        )
                    )
                    result = boolean_point_in_polygon(point, cc)
                    if result:
                        matched_service.append(service.pk)

            queryset = queryset.filter(pk__in=matched_service)
        return queryset


class ServiceViewSet(viewsets.ModelViewSet):
    serializer_class = ServiceSerializer
    permission_classes = [permissions.IsAuthenticated]
    filter_backends = [DjangoFilterBackend, AddressFilterBackend]
    filterset_fields = ["providerType"]

    def get_queryset(self):
        """
        This view should return a list of all the purchases
        for the currently authenticated user.
        """
        queryset = Service.objects.all()
        username = self.request.query_params.get("user")
        if username is not None:
            queryset = queryset.filter(user=username)
        return queryset

    def get_permissions(self, *args, **kwargs):
        if self.action in ["list", "retrieve"]:
            return [permissions.AllowAny()]

        return [permission_class() for permission_class in self.permission_classes]


class ServiceAddressViewSet(viewsets.ModelViewSet):
    queryset = ServiceAddress.objects.all()
    serializer_class = ServiceAddressSerializer
    permission_classes = [permissions.IsAuthenticated]


class AppointmentViewSet(viewsets.ModelViewSet):
    queryset = Appointment.objects.all()
    serializer_class = AppointmentSerializer
    permission_classes = [permissions.IsAuthenticated]
