from rest_framework import viewsets, permissions

from ecare.role.models import Role
from ecare.role.serializers import RoleSerializer


class RoleViewSet(viewsets.ReadOnlyModelViewSet):
    """
    API endpoint that allows users to be viewed.
    """

    queryset = Role.objects.all()
    serializer_class = RoleSerializer
    permission_classes = [permissions.AllowAny]
