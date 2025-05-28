from .models import city, menu
from .serializers import citySerializer, menuSerializer
from rest_framework import viewsets


class cityViewSet(viewsets.ModelViewSet):
    queryset = city.objects.all()
    serializer_class = citySerializer

class menuViewSet(viewsets.ModelViewSet):
    queryset = menu.objects.all()
    serializer_class = menuSerializer
