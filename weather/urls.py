from django.urls import include, path
from rest_framework.routers import DefaultRouter

from weather.views import CityView

router = DefaultRouter()
router.register(r'cities', CityView)

urlpatterns = [
    path('', include(router.urls)),
]
