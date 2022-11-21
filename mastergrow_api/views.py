from django.shortcuts import render
from mastergrow_api import serializers
from rest_framework import viewsets
from rest_framework.settings import api_settings
from .models import Plants, BaseNutrients


class PlantsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class= serializers.PlantsSerializer
    queryset = Plants.objects.all()
  
class BaseNutrientsViewSet(viewsets.ModelViewSet):
    """Handle creating and updating profiles"""
    serializer_class= serializers.BaseNutrientsSerializer
    queryset = BaseNutrients.objects.all()