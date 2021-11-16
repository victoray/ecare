from rest_framework import serializers

from ecare.service.models import Service, Address, ServiceAddress, Appointment
from ecare.user.serializers import UserSerializer


class ServiceAddressSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = ServiceAddress
        fields = ["latitude", "longitude", "rawAddress", "url", "uuid", "service"]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    addresses = ServiceAddressSerializer(many=True)
    user = UserSerializer()

    class Meta:
        model = Service
        fields = [
            "fullDescription",
            "images",
            "name",
            "pricePerHour",
            "providerType",
            "shortDescription",
            "url",
            "user",
            "uuid",
            "addresses",
        ]
        read_only_fields = ["user"]


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = UserSerializer()
    careProvider = UserSerializer()

    class Meta:
        model = Appointment
        fields = ["service", "patient", "appointmentDate", "careProvider", "uuid"]
