# Generated by Django 4.1.7 on 2023-03-16 02:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CertificationType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='ImagesProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image_project', models.ImageField(upload_to='static_dirs/images/project_image')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('const', models.DecimalField(decimal_places=10, max_digits=12)),
                ('work_history_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Portfilo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('linkVide', models.URLField()),
                ('description', models.CharField(max_length=50)),
                ('images', models.ManyToManyField(null=True, to='authentication.imagesproject')),
                ('portfilo_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Certifications',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('Issue_date', models.DateField()),
                ('Expiration_date', models.DateField()),
                ('Certification_ID', models.CharField(max_length=50)),
                ('Certification_UR', models.CharField(max_length=100)),
                ('certifications_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
    ]
