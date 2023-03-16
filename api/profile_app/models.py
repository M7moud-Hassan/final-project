from django.db import models

from authentication.models import RegisterFreelancer


# Create your models here.


class WorkHistory(models.Model):
    id = models.AutoField
    work_history_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    const = models.DecimalField(decimal_places=5, max_digits=10)

class ImagesProject(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to='media/images/project_image', blank=True, null=True)


class Portflio(models.Model):
    id = models.AutoField
    portflio_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    images = models.ManyToManyField(ImagesProject, null=True,blank=True)
    linkVide = models.URLField(null=True)
    description = models.CharField(max_length=500)


class CertificationType(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)


class Certification(models.Model):
    id = models.AutoField
    certification_user_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    issuse_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    certification_ID = models.CharField(max_length=50)
    certification_UR = models.CharField(max_length=100)