# Generated by Django 4.1.7 on 2023-04-19 05:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0006_remove_contact_ad_type'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='ad_type',
            field=models.CharField(choices=[('Search Engine Optimization ', 'Search Engine Optimization '), ('Social Media Marketing', 'Social Media Marketing'), ('Email Marketing', 'Email Marketing'), ('Pay-Per-Click Advertising', 'Pay-Per-Click Advertising'), ('Data Analytics', 'Data Analytics')], default='Outdoor Advertising', max_length=128),
        ),
    ]
