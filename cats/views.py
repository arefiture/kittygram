from rest_framework import viewsets

from .models import Cat
from .serializers import CatSerializer


class CatViewSet(viewsets.ModelViewSet):
    queryset = Cat.objects.all()
    serializer_class = CatSerializer

    # Если же queryset задан неявно через get_queryset
    # То basename нужно ОБЯЗАТЕЛЬНО указывать явным образом
