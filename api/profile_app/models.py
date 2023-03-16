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


class CertificationType(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)


class Certification(models.Model):
    id = models.AutoField
    id_user_free = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    Issuse_date = models.DateField
    Expiration_date = models.DateField
    Certification_ID = models.CharField(max_length=50)
    Certification_UR = models.CharField(max_length=100)