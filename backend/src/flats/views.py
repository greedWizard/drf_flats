from rest_framework import serializers
from rest_framework.response import Response
from flats.serializers import FlatPostSerializer, FlatReadSerializer
from base.views import ServiceViewSet
from .services import AdressService
from users.serializers import UserReadSerializer

from drf_spectacular.utils import extend_schema_view

from rest_framework.permissions import IsAuthenticated


class FlatViewSet(ServiceViewSet):
    ''' Flat ViewSet '''
    service = AdressService
    read_serializer = FlatReadSerializer
    action_serializer = FlatPostSerializer
    permission_classes = (IsAuthenticated, )
    user_serializer = UserReadSerializer

    def list(self, request, *args, **kwargs):
        objects = self.service().fetch(
            page=self.request.query_params.get('page', 0),
            user_id=request.user.id,
        )
        serializer = self.read_serializer(objects, many=True)

        return Response(
            serializer.data
        )