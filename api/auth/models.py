from django.db import models

# Create your models here.


class CategoryService (models.Model):
    name = models.CharField(max_length=50)
    id = models.autoField()


class Services (models.Model):
    id = models.AutoField
    name = models.CharField(50)
    category_service = models.ForeignKey(CategoryService, on_delete=models.CASCADE)


class Experience (models.Model):
    title = models.CharField(50, required=True)
    company = models.CharField(100, required=True)
    location = models.CharField(200, required=False)
    is_current_work_in_company = models.BooleanField(default=False)
    start_date = models.DateField()
    end_date = models.DateField()
    description = models.CharField(500)
    id = models.AutoField


class Education (models.Model):
    school = models.CharField(50)
    degree = models.CharField(100)
    study = models.CharField(100)
    from_year = models.IntegerField(4)
    to_year = models.IntegerField(4)
    description = models.var(500)
    id = models.AutoField
