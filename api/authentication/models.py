from django.db import models

# Create your models here.


class CategoryService (models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)

class Services (models.Model):
    id = models.AutoField
    name = models.CharField(max_length=50)
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE)


class Experience (models.Model):
    title = models.CharField(max_length=50)
    company = models.CharField(max_length=100)
    location = models.CharField(max_length=200)
    is_current_work_in_company = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(max_length=500)
    id = models.AutoField


class Education (models.Model):
    school = models.CharField(max_length=50)
    degree = models.CharField(max_length=100)
    study = models.CharField(max_length=100)
    from_year = models.IntegerField(4)
    to_year = models.IntegerField(4)
    description = models.CharField(max_length=500)
    id = models.AutoField

