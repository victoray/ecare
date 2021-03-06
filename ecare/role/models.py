from django.db import models

from ecare.core.models import AbstractBaseModel


class Role(AbstractBaseModel):
    PATIENT = "patient"
    PROVIDER = "provider"

    TYPE_CHOICES = [
        (PATIENT, "Patient"),
        (PROVIDER, "Provider"),
    ]
    name = models.CharField(max_length=255)
    type = models.CharField(
        max_length=255,
        choices=TYPE_CHOICES,
    )

    def is_patient(self):
        return self.type == self.PATIENT

    def is_provider(self):
        return self.type == self.PROVIDER

    class Meta:
        unique_together = ("name", "type")
