from django.db import models

# Create your models here.
class CategoryService(models.Model):
    name = models.CharField(max_length=50)
    id = models.AutoField(primary_key=True)

class Services(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)
    category_service = models.ForeignKey(CategoryService)


class Experience(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=50,null=False)
    company = models.CharField(max_length=100,null=False)
    location = models.CharField(max_length=200,null=True)
    is_current_work_in_company = models.BooleanField(default=False)
    description = models.CharField(max_length=500)


class Education(models.Model):
    id = models.AutoField(primary_key=True)
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    field_study = models.CharField(max_length=100)
    description = models.CharField(max_length=500)



class Skills(models.Models):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class JobTitle (models.Models):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=50)


class RegisterFreelancer(models.Models):
    id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=100)
    is_active = models.BooleanField(default=False)
    phone_number = models.CharField(max_length=11)
    password = models.CharField(max_length=300, null=False)
    job_title = models.ForeignKey(JobTitle, on_delete=models.CASCADE)
    overview = models.CharField(max_length=500)
    hourly_rate = models.DoubleField(null=True)
    user_image = models.ImageField(upload_to='static/static_dirs/images/user_image')
    street_address = models.CharField(max_length=200)
    city = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    postal_code = models.CharField(max_length=20)
    experience = models.ManyToManyField(Experience)
    education = models.ManyToManyField(Education)
    skills = models.ManyToManyField(Skills)
    services = models.ManyToManyField(Services)



