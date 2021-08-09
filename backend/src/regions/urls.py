from rest_framework.routers import DefaultRouter
from .views import CityViewSet, StateViewSet


router = DefaultRouter()

router.register('cities', CityViewSet, basename='cities')
router.register('states', StateViewSet, 'states')

urlpatterns = router.urls