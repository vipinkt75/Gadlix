# Generated by Django 4.1.7 on 2023-04-27 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0009_alter_contact_ad_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='ad_type',
            field=models.CharField(choices=[('Search Engine Optimization ', 'Search Engine Optimization '), ('Social Media Marketing', 'Social Media Marketing'), ('Email Marketing', 'Email Marketing'), ('Pay-Per-Click Advertising', 'Pay-Per-Click Advertising'), ('Data Analytics', 'Data Analytics')], default='Outdoor Advertising', max_length=128),
        ),
    ]
