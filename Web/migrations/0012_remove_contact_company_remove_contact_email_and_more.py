# Generated by Django 4.1.7 on 2023-05-01 07:04

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0011_remove_contact_ad_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='company',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='email',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='phone',
        ),
        migrations.RemoveField(
            model_name='contact',
            name='website',
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(choices=[('', 'Select Services'), ('DigitalMarketing', 'Digital Marketing'), ('MobileAppDevelopment', 'Mobile App Development'), ('WebApplicationDevelopment', 'Web Application Development'), ('EcommerceDevelopment', 'Ecommerce Development'), ('WebsiteDevelopment', 'Website Development')], max_length=30, unique=True),
        ),
    ]
