# Generated by Django 4.2.1 on 2023-05-11 06:10

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0013_contact_services_contact_company_contact_email_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='Services',
            field=models.CharField(choices=[('', 'Select Services'), ('Search Engine Optimization ', 'Search Engine Optimization '), ('Social Media Marketing', 'Social Media Marketing'), ('Email Marketing', 'Email Marketing'), ('Pay-Per-Click Advertising', 'Pay-Per-Click Advertising'), ('Data Analytics', 'Data Analytics')], max_length=254, null=True),
        ),
    ]
