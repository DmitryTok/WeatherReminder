from rest_framework import mixins, viewsets
from rest_framework.permissions import AllowAny

from users.models import City
from weather.serializers import CitySerializer


class ListCreateDeleteViewSet(mixins.CreateModelMixin,
                              mixins.ListModelMixin,
                              mixins.DestroyModelMixin,
                              viewsets.GenericViewSet):
    pass


class CityView(ListCreateDeleteViewSet):
    queryset = City.objects.all()
    serializer_class = CitySerializer
    permission_classes = [AllowAny, ]
    pagination_class = None
