
from rest_framework.serializers import ModelSerializer
from data.models import Thing, SubThing, UnrelatedThing


class ThingSerializer(ModelSerializer):
    class Meta:
        model = Thing
        fields = '__all__'


class SubThingSerializer(ModelSerializer):
    class Meta:
        model = SubThing
        fields = '__all__'


class UnrelatedThingSerializer(ModelSerializer):
    class Meta:
        model = UnrelatedThing
        fields = '__all__'
