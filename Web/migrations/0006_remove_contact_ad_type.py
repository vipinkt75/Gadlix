# Generated by Django 4.1.7 on 2023-04-19 05:18

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0005_alter_contact_ad_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='contact',
            name='ad_type',
        ),
    ]
