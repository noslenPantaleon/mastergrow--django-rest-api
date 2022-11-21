from rest_framework.serializers import ModelSerializer
from .models import Plants, BaseNutrients

class PlantsSerializer(ModelSerializer):
    class Meta:
        model= Plants
        fields= '__all__'


class BaseNutrientsSerializer(ModelSerializer):
    class Meta:
        model= BaseNutrients
        fields= '__all__'