from copy import copy
from typing import OrderedDict

from rest_framework import serializers

from ecare.service.models import Service, Address, ServiceAddress, Appointment
from ecare.user.models import User
from ecare.user.serializers import UserSerializer


class ServiceAddressSerializer(serializers.HyperlinkedModelSerializer):
    service = serializers.UUIDField(allow_null=True, required=False)

    class Meta:
        model = ServiceAddress
        fields = ["latitude", "longitude", "rawAddress", "url", "uuid", "service"]


class ServiceSerializer(serializers.HyperlinkedModelSerializer):
    addresses = ServiceAddressSerializer(many=True)
    user = UserSerializer(read_only=True)

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
            "user_id",
        ]
        read_only_fields = ["user"]

    def create(self, validated_data):
        data = copy(validated_data)
        data.pop("addresses")
        request = self.context.get("request")
        service = Service(**data, user=request.user)

        return service

    def save(self, **kwargs):
        service = super(ServiceSerializer, self).save()
        service.save()

        addresses: list[OrderedDict] = self.validated_data.pop("addresses")

        for address in addresses:
            ServiceAddress(**address, service=service).save()


class AppointmentSerializer(serializers.HyperlinkedModelSerializer):
    patient = UserSerializer()
    careProvider = UserSerializer()

    class Meta:
        model = Appointment
        fields = ["service", "patient", "appointmentDate", "careProvider", "uuid"]
