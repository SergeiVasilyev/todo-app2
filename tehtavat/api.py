# API - Application Programming Interface

from rest_framework import routers, serializers, viewsets

from .models import Tehtava

class TehtavaSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Tehtava
        fields = ['id', 'otsikko', 'tehty']

class TehtavaViewSet(viewsets.ModelViewSet):
    queryset = Tehtava.objects.all()
    # queryset = Tehtava.objects.filter(id=1)
    serializer_class = TehtavaSerializer


