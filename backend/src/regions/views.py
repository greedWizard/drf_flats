from drf_spectacular.utils import extend_schema, extend_schema_view
from base.views import ServiceViewSet
from .services import StateService, CityService
from .serializers import CityPostSerializer, CityReadSerializer, StatePostSerializer, StateReadSerializer


class CityViewSet(ServiceViewSet):
    service = CityService
    read_serializer = CityReadSerializer
    action_serializer = CityPostSerializer


class StateViewSet(ServiceViewSet):
    service = StateService
    read_serializer = StateReadSerializer
    action_serializer = StatePostSerializer
