import uuid

from django.core.exceptions import ValidationError
from django.shortcuts import render, get_object_or_404

# Create your views here.
from rest_framework import viewsets, permissions
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from ecare.core.permissions import IsOwner
from ecare.user.models import User
from ecare.user.serializers import UserSerializer


class UserViewSet(viewsets.ModelViewSet):
    """
    API endpoint that allows users to be viewed or edited.
    """

    queryset = User.objects.all()
    serializer_class = UserSerializer
    permission_classes = [permissions.IsAuthenticated]

    def retrieve(self, request, *args, **kwargs):
        uid = kwargs.get("pk")
        try:
            user = get_object_or_404(self.queryset, pk=uid)
        except ValidationError:
            user = get_object_or_404(self.queryset, username=uid)

        serializer = self.get_serializer(user)
        return Response(serializer.data)
