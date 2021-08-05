from rest_framework import urlpatterns
from rest_framework.routers import DefaultRouter
from .views import FlatViewSet


router = DefaultRouter()

router.register('adresses', FlatViewSet, basename='adresses')

urlpatterns = router.urls