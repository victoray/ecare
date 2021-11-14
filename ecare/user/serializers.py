from rest_framework import serializers

from ecare.user.models import User


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = [
            "uuid",
            "email",
            "username",
            "legalName",
            "gender",
            "dateOfBirth",
            "emergencyContact",
            "governmentId",
            "profileImage",
            "role",
        ]
        read_only_fields = ("email", "uuid", "username")
