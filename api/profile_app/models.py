from django.db import models

from authentication.models import RegisterFreelancer

from authentication.models import RegisterUser
# Create your models here.
class Employment_History(models.Model):
    id = models.AutoField
    id_free = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    company = models.CharField(max_length=50)
    location = models.CharField(max_length=50)
    title = models.CharField(max_length=200)
    period_from_month = models.CharField(max_length=50)
    period_to_month = models.CharField(max_length=50, null=True)
    is_current_work = models.BooleanField(default=False)
    description = models.CharField(max_length=500, null=True)

class WorkHistory(models.Model):
    id = models.AutoField
    work_history_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    location = models.CharField(max_length=100)
    date = models.DateField()
    cost = models.DecimalField(decimal_places=5, max_digits=10)


class ImagesProject(models.Model):
    id = models.AutoField
    image = models.ImageField(upload_to='images/Portflio_images/', null=True)


class Portflio(models.Model):
    id = models.AutoField
    portflio_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    title = models.CharField(max_length=100)
    date_time=models.DateField(null=True)
    images = models.ManyToManyField(ImagesProject, null=True, blank=True)
    linkVide = models.URLField(null=True)
    description = models.CharField(max_length=500)


class CertificationType(models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    def __str__(self):
        return self.name


class Certification(models.Model):
    id = models.AutoField
    certification_user_freelancer = models.ForeignKey(RegisterFreelancer, on_delete=models.CASCADE)
    provider = models.CharField(max_length=50)
    description = models.CharField(max_length=500)
    issuse_date = models.DateField(null=True)
    expiration_date = models.DateField(null=True)
    certification_ID = models.CharField(max_length=50)
    certification_UR = models.CharField(max_length=100)
    certification_type = models.ForeignKey(CertificationType, on_delete=models.CASCADE)


class PaymentMethod(models.Model):
    id = models.AutoField
    nameOnTheCard = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city =models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    Zip_code = models.CharField(max_length=30)
    Expire_year = models.IntegerField(4)
    Expire_month = models.IntegerField(max_length=2)
    Credit_number = models.IntegerField(16)
    CVV = models.IntegerField(3)
    client_id = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)


class PaymentFreeMethod(models.Model):
    id = models.AutoField
    nameOnTheCard = models.CharField(max_length=50)
    email = models.EmailField(max_length=50)
    city =models.CharField(max_length=30)
    state = models.CharField(max_length=30)
    Zip_code = models.CharField(max_length=30)
    Expire_year = models.IntegerField(4)
    Expire_month = models.IntegerField(max_length=2)
    Credit_number = models.IntegerField(16)
    CVV = models.IntegerField(3)
    client_id = models.ForeignKey(RegisterUser, on_delete=models.CASCADE)
