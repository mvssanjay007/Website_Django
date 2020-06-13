from django.db import models


# Create your models here.
class Subjects(models.Model):
    des= models.CharField(max_length=200)
    img= models.ImageField(upload_to='pics')
    name= models.CharField(max_length=200)
    trend= models.BooleanField(default=False)
    keys= models.CharField(max_length=200)
    down= models.CharField(max_length=200)
