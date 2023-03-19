# Generated by Django 4.1.7 on 2023-03-19 12:23

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

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
                ('image', models.ImageField(null=True, upload_to='images/Portflio_images/')),
            ],
        ),
        migrations.CreateModel(
            name='WorkHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('location', models.CharField(max_length=100)),
                ('date', models.DateField()),
                ('cost', models.DecimalField(decimal_places=5, max_digits=10)),
                ('work_history_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Portflio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=100)),
                ('linkVide', models.URLField(null=True)),
                ('description', models.CharField(max_length=500)),
                ('images', models.ManyToManyField(blank=True, null=True, to='profile_app.imagesproject')),
                ('portflio_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Payment',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.CharField(max_length=150)),
                ('street_address', models.CharField(max_length=50)),
                ('city', models.CharField(max_length=50)),
                ('state', models.CharField(max_length=50)),
                ('postal_code', models.CharField(max_length=20)),
                ('name_on_card', models.CharField(max_length=50)),
                ('credit_card_number', models.CharField(max_length=20)),
                ('exp_month', models.DateField()),
                ('exp_year', models.DateField()),
                ('cvv', models.IntegerField(max_length=5)),
                ('payment_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Employment_History',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('company', models.CharField(max_length=50)),
                ('location', models.CharField(max_length=50)),
                ('title', models.CharField(max_length=200)),
                ('period_from_month', models.CharField(max_length=50)),
                ('period_to_month', models.CharField(max_length=50, null=True)),
                ('is_current_work', models.BooleanField(default=False)),
                ('description', models.CharField(max_length=500, null=True)),
                ('id_free', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
        migrations.CreateModel(
            name='Certification',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('provider', models.CharField(max_length=50)),
                ('description', models.CharField(max_length=500)),
                ('issuse_date', models.DateField(null=True)),
                ('expiration_date', models.DateField(null=True)),
                ('certification_ID', models.CharField(max_length=50)),
                ('certification_UR', models.CharField(max_length=100)),
                ('certification_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile_app.certificationtype')),
                ('certification_user_freelancer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='authentication.registerfreelancer')),
            ],
        ),
    ]
