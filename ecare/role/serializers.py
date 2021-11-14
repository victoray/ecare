from rest_framework import serializers

from ecare.role.models import Role


class RoleSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Role
        fields = "__all__"
