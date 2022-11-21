from django.urls import path, include
from mastergrow_api import views
from rest_framework.routers import DefaultRouter

router= DefaultRouter()

router.register('plants', views.PlantsViewSet)
router.register('nutrients', views.BaseNutrientsViewSet)

urlpatterns= [

    path('',  include(router.urls))
]