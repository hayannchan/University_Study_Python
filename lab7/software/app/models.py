from django.db import models
from django.urls import reverse

class Corporation(models.Model):
    id_c = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    year = models.IntegerField()
    # представление объекта модели текстом
    def __str__(self):
        return f"{self.name}, {self.year}"
    
class Software(models.Model):
    id_s = models.AutoField(primary_key=True)
    name = models.CharField(max_length=30)
    developer = models.ForeignKey(Corporation, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.name}, {self.developer}"
    
class Version(models.Model):
    id_v = models.AutoField(primary_key=True)
    version = models.CharField(max_length=30)
    soft_name = models.ForeignKey(Software, on_delete=models.CASCADE)
    def __str__(self):
        return f"{self.version}, {self.soft_name}"