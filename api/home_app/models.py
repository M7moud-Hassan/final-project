from datetime import datetime

from django.db import models

from authentication.models import Skills, RegisterFreelancer

from authentication.models import RegisterUser


# Create your models here.

class JobImages(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to='images/images_job/')


class LikeJob(models.Model):
    id = models.AutoField
    id_free = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)


class DisLike(models.Model):
    id = models.AutoField
    id_free = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)

class Job(models.Model):
    id = models.AutoField
    create_at = models.DateTimeField(default=datetime.now, blank=True)
    title = models.CharField(max_length=50)
    cost = models.DecimalField(decimal_places=2, max_digits=10)
    images = models.ManyToManyField(JobImages, blank=True)
    description = models.CharField(max_length=1000)
    skills = models.ManyToManyField(Skills, blank=True)
    Proposals = models.ManyToManyField(RegisterFreelancer, blank=True)
    is_pyment = models.BooleanField(default=False)
    likes = models.ManyToManyField(LikeJob, blank=True)
    dislikes = models.ManyToManyField(DisLike, blank=True)
    client_id = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)

