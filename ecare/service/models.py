from django.contrib.postgres.fields import ArrayField
from django.db import models
from twilio.twiml.voice_response import Room

from ecare.core.models import AbstractBaseModel
from ecare.user.models import User

healthCareProviders = [
    {"value": "doctor", "label": "Doctor"},
    {"value": "nurse", "label": "Nurse"},
    {"value": "therapist", "label": "Therapist"},
    {"value": "dentist", "label": "Dentist"},
    {"value": "pharmacist", "label": "Pharmacist"},
    {"value": "physicalTherapist", "label": "Physical Therapist"},
    {"value": "medLabScientist", "label": "Medical Laboratory Scientist"},
    {"value": "hospital", "label": "Hospital"},
    {"value": "careHome", "label": "Care Home"},
    {"value": "ophthalmologist", "label": "Ophthalmologist"},
    {"value": "podiatrist", "label": "Podiatrist"},
    {"value": "other", "label": "Other"},
]


class Service(AbstractBaseModel):
    PROVIDER_TYPE_CHOICES = [
        (provider.get("value"), provider.get("label"))
        for provider in healthCareProviders
    ]
    name = models.CharField(max_length=255)
    shortDescription = models.TextField()
    fullDescription = models.TextField()
    images = ArrayField(models.URLField())
    user = models.ForeignKey(User, on_delete=models.PROTECT)
    providerType = models.CharField(max_length=255, choices=PROVIDER_TYPE_CHOICES)
    pricePerHour = models.FloatField()


class Address(AbstractBaseModel):
    rawAddress = models.TextField()
    longitude = models.FloatField()
    latitude = models.FloatField()

    class Meta:
        abstract = True


class ServiceAddress(Address):
    service = models.ForeignKey(
        Service, related_name="addresses", on_delete=models.CASCADE
    )


class Appointment(AbstractBaseModel):
    service = models.ForeignKey(
        Service, related_name="appointments", on_delete=models.PROTECT
    )
    patient = models.ForeignKey(
        User, related_name="patientAppointments", on_delete=models.PROTECT
    )
    careProvider = models.ForeignKey(
        User, related_name="careProviderAppointments", on_delete=models.PROTECT
    )
    appointmentDate = models.DateTimeField()
