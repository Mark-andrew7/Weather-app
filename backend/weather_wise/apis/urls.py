from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TemperatureViewSet, WindViewSet

router = DefaultRouter()
router.register(r'temperatures', TemperatureViewSet)
router.register(r'winds', WindViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
