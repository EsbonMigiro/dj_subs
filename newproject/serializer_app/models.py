from django.db import models

# Create your models here.

class SerializerModel(models.Model):
    email = models.EmailField()
    password = models.CharField(max_length=255)

