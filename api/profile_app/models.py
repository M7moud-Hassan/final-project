from django.db import models

from models import RegisterFreelancer


# Create your models here.


class Work_History(models.Model):
    id = models.AutoField
    id = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    cons = models.DecimalField()

class imagesProject(models.Model):
    id = models.AutoField
    image = models.ImageField


class portflio(models.Model):
    id = models.AutoField
    id = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    images = models.ManyToManyField(imagesProject)
    linkVide = models.URLField()
    description = models.CharField(max_length=500)