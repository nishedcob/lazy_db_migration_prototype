
from django.shortcuts import render
from rest_framework.viewsets import ReadOnlyModelViewSet

from data.models import Thing, SubThing, UnrelatedThing
from data.serializers import ThingSerializer, SubThingSerializer, UnrelatedThingSerializer

# Create your views here.

class ThingViewSet(ReadOnlyModelViewSet):
    queryset = Thing.objects.all()
    serializer_class = ThingSerializer

class SubThingViewSet(ReadOnlyModelViewSet):
    queryset = SubThing.objects.all()
    serializer_class = SubThingSerializer

class UnrelatedThingViewSet(ReadOnlyModelViewSet):
    queryset = UnrelatedThing.objects.all()
    serializer_class = UnrelatedThingSerializer
