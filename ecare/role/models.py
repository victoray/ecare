from django.db import models


class Role(models.Model):
    PATIENT = "patient"
    PROVIDER = "provider"

    TYPE_CHOICES = [
        (PATIENT, "Patient"),
        (PROVIDER, "Provider"),
    ]
    name = models.CharField()
    type = models.CharField(choices=TYPE_CHOICES)

    def is_patient(self):
        return self.type == self.PATIENT

    def is_provider(self):
        return self.type == self.PROVIDER
