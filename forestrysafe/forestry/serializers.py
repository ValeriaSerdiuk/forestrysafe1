from .models import Forestry, Animal, Feeder, Vaccination
from rest_framework import serializers


class ForestrySerializer(serializers.ModelSerializer):
    class Meta:
        model = Forestry
        fields = '__all__'


class AnimalSerializer(serializers.ModelSerializer):
    class Meta:
        model = Animal
        fields = '__all__'


class FeederSerializer(serializers.ModelSerializer):
    class Meta:
        model = Feeder
        fields = '__all__'


class FeederCreateSerializer(FeederSerializer):
    feeder_more = FeederSerializer(required=True)

    class Meta(FeederSerializer.Meta):
        model = Feeder
        fields = FeederSerializer.Meta.fields + ['feeder']

    def create(self, validated_data):
        feeder_data = validated_data.pop('feeder')
        feeder = Feeder.objects.create_user(**validated_data)
        Feeder.objects.create(user=feeder, **feeder_data)
        return feeder


class VaccinationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Vaccination
        fields = '__all__'
