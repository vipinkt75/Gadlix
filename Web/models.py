from django.db import models
from tinymce.models import HTMLField
from versatileimagefield.fields import PPOIField, VersatileImageField


class Service(models.Model):
    title = models.CharField(max_length=225)
    summary = models.CharField(max_length=355)
    content = HTMLField(blank=True, null=True)
    image = VersatileImageField("Image", upload_to="services/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    description = models.TextField()

    def __str__(self):
        return self.title


# class Term(models.Model):
#     service=models.ForeignKey(Service,on_delete=models.CASCADE)
#     term=HTMLField(blank=True,null=True)


class Gallery(models.Model):
    title = models.CharField(max_length=225)
    image = VersatileImageField("Image", upload_to="gallery/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    class Meta:
        verbose_name_plural = "Gallery"

    def __str__(self):
        return str(self.title)


class Update(models.Model):
    title = models.CharField(max_length=225)
    summary = models.CharField(max_length=500)
    date = models.DateField()
    image = VersatileImageField("Image", upload_to="updates/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")
    content = HTMLField(blank=True, null=True)
    slug = models.SlugField(unique=True)

    def __str__(self):
        return str(self.title)


class Client(models.Model):
    title = models.CharField(max_length=225)
    image = VersatileImageField("Image", upload_to="clients/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    def __str__(self):
        return str(self.title)


class Testimonial(models.Model):
    decription = models.CharField(max_length=500)
    name = models.CharField(max_length=225)
    designation = models.CharField(max_length=225)
    image = VersatileImageField("Image", upload_to="testimonials/", ppoi_field="ppoi")
    ppoi = PPOIField("Image PPOI")

    def __str__(self):
        return str(self.name)


# class Contact(models.Model):
#     AD_CHOICES = [
#         ('Search Engine Optimization ', 'Search Engine Optimization '),
#         ('Social Media Marketing', 'Social Media Marketing'),
#         ('Email Marketing', 'Email Marketing'),
#          ('Pay-Per-Click Advertising', 'Pay-Per-Click Advertising'),
#          ('Data Analytics', 'Data Analytics'),
#     ]
#     ad_type = models.CharField(max_length=4, choices=AD_CHOICES)
#     name = models.CharField(max_length=225)
#     company = models.CharField(max_length=225)
#     phone = models.CharField(max_length=12)
#     email = models.EmailField()
#     website = models.CharField(max_length=225)
#     ad_type = models.CharField(
#         max_length=128, choices=AD_CHOICES, default="Outdoor Advertising"
#     )

#     def __str__(self):
#         return str(self.name)

STATUS_CHOICHES = [
        ("", 'Select Services'),
        ('Search Engine Optimization ', 'Search Engine Optimization '),
        ('Social Media Marketing', 'Social Media Marketing'),
        ('Email Marketing', 'Email Marketing'),
        ('Pay-Per-Click Advertising', 'Pay-Per-Click Advertising'),
        ('Data Analytics', 'Data Analytics'),
]

class Contact(models.Model):
    name = models.CharField(max_length=225)
    company = models.CharField(max_length=225)
    phone = models.CharField(max_length=12)
    email = models.EmailField()
    website = models.CharField(max_length=225)
    Services = models.CharField(max_length=254, choices=STATUS_CHOICHES, null=True)

    def __str__(self):
        return str(self.name)
    
# class Contact(models.Model):
#     name = models.CharField(max_length=30, choices=STATUS_CHOICHES, unique=True)

#     def __str__(self):
#         return self.name