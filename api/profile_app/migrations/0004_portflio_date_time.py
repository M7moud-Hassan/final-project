# Generated by Django 4.1.7 on 2023-03-20 12:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0003_paymentmethod_client_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='portflio',
            name='date_time',
            field=models.DateField(default='1996-12-12'),
            preserve_default=False,
        ),
    ]