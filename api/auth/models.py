from django.db import models

class Skills(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField

class JobTitle(models.Model):
    name=models.CharField(max_length=50)
    id=models.AutoField
class RegisterFreelancer(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email=models.CharField(max_length=100)
    is_active=models.BooleanField(default=False)
    phone_number=models.CharField(max_length=11)
    password=models.CharField(max_length=300)
    job_title=models.ForeignKey(JobTitle,on_delete=models.CASCADE)
    overview=models.CharField(max_length=500)
    hourly_rate=models.DoubleField(null=True)
    user_image=models.ImageField(upload_to='static_dirs/images/user_image')
    street_address=models.CharField(max_length=50)
    city=models.CharField(max_length=50)
    state=models.CharField(max_length=50)
    postal_code=models.CharField(max_length=20)
    experience=models.ManyToManyField(Experience)
    education=models.ManyToManyField(Education)
    skills=models.ManyToManyField(Skills)
    services=models.ManyToManyField(Services)




