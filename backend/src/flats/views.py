from flats.serializers import FlatPostSerializer, FlatReadSerializer
from base.views import ServiceViewSet
from .services import AdressService

from drf_spectacular.utils import extend_schema_view


@extend_schema_view(
    tags='flats'
)
class FlatViewSet(ServiceViewSet):
    ''' Flat ViewSet '''
    service = AdressService
    read_serializer = FlatReadSerializer
    action_serializer = FlatPostSerializer
