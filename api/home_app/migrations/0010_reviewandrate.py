# Generated by Django 4.1.7 on 2023-03-26 20:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('authentication', '0001_initial'),
        ('home_app', '0009_job_is_hire'),
    ]

    operations = [
        migrations.CreateModel(
            name='ReviewAndRate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rate', models.IntegerField(max_length=5)),
                ('review', models.CharField(max_length=5000)),
                ('free', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
    ]
