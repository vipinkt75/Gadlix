# Generated by Django 4.1.7 on 2023-05-01 07:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Web', '0012_remove_contact_company_remove_contact_email_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='contact',
            name='Services',
            field=models.CharField(blank=True, choices=[('', 'Select Services'), ('DigitalMarketing', 'Digital Marketing'), ('MobileAppDevelopment', 'Mobile App Development'), ('WebApplicationDevelopment', 'Web Application Development'), ('EcommerceDevelopment', 'Ecommerce Development'), ('WebsiteDevelopment', 'Website Development')], max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='contact',
            name='company',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='email',
            field=models.EmailField(default=0, max_length=254),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='phone',
            field=models.CharField(default=0, max_length=12),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='contact',
            name='website',
            field=models.CharField(default=0, max_length=225),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='contact',
            name='name',
            field=models.CharField(max_length=225),
        ),
    ]