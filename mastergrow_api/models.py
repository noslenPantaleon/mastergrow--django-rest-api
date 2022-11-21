from django.db import models

# Create your models here.

class Plants(models.Model):
    growName= models.CharField(max_length=255, unique = True)
    plantName= models.CharField(max_length= 255, primary_key=True)
    hydroponics=models.BooleanField()
    sustrate= models.BooleanField()
    created_on= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return self.growName

class BaseNutrients(models.Model):
    plantGrowing=models.ForeignKey(
        Plants,
        on_delete=models.CASCADE,
    )
    Macronutrients= models.IntegerField(blank=True, null=True)
    Micronutrients= models.IntegerField(blank=True, null=True)
    silicio= models.IntegerField(blank=True, null=True)
    mycorrhizae=  models.IntegerField(blank=True, null=True)
    trichodermas= models.IntegerField(blank=True, null=True)
    BloomFlowering= models.IntegerField(blank=True, null=True)
    rootBiostimulant=models.IntegerField(blank=True, null=True)
    notes= models.CharField(max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)


class PruningPlant(models.Model):
    
 
    Plantpruning=models.ForeignKey(
        Plants,
        on_delete=models.CASCADE,)
    pruning= models.BooleanField(default=False)
    notes= models.CharField(max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)
   
    
class Pesticides(models.Model):
    plantPesticide=models.ForeignKey(
        Plants,
        on_delete=models.CASCADE,)
    pesticides= models.BooleanField(default=False)
    notes= models.CharField(max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)


class PlantsDisease (models.Model):
    plantsDisease=models.ForeignKey(
        Plants,
        on_delete=models.CASCADE,)
    disease= models.BooleanField(default=False)
    notes= models.CharField(max_length=255)
    created_on= models.DateTimeField(auto_now_add=True)