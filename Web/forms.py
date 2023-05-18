# from django import forms
# from django.forms.widgets import (CheckboxInput, EmailInput, FileInput,
#                                   NumberInput, RadioSelect, Select,
#                                   SelectMultiple, Textarea, TextInput,
#                                   URLInput)

# from .models import Contact


# class ContactForm(forms.ModelForm):
#     class Meta:
#         model = Contact
#         fields = "__all__"
#         widgets = {
#             "name": TextInput(
#                 attrs={"class": "required form-control", "placeholder": "Name"}
#             ),
#             "company": TextInput(
#                 attrs={"class": "required form-control", "placeholder": "Company"}
#             ),
#             "phone": TextInput(
#                 attrs={"class": "required form-control", "placeholder": "Phone"}
#             ),
#             "email": EmailInput(
#                 attrs={"class": "form-control", "placeholder": "Email"}
#             ),
#             "website": TextInput(
#                 attrs={"class": "form-control", "placeholder": "Website"}
#             ),
#             "ad_type": RadioSelect(
#                 attrs={"id": "html", "name": "fav", "value": "Outdoor_Advertising"}
#             ),
#             # 'ad_type':RadioSelect(attrs={'id':"css", 'name':"fav" ,'value':"Agency_Partnership"}),
#         }

from django import forms
from django.utils.translation import gettext_lazy as _
from .models import Contact
from django.forms import widgets
from django.forms.widgets import (CheckboxInput, EmailInput, FileInput,
                                  NumberInput, RadioSelect, Select,
                                  SelectMultiple, Textarea, TextInput,
                                  URLInput)


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        exclude = ("timestamp",)
        widgets = {
            "name": TextInput(
                attrs={"class": "required form-control ",
                       "placeholder": "Name"}
            ),
            "company": TextInput(
                attrs={"class": "required form-control ",
                       "placeholder": "Company"}
            ),
            "phone": TextInput(
                attrs={"class": "required form-control",
                       "placeholder": "Phone"}
            ),
            "email": EmailInput(
                attrs={"class": "form-control", "placeholder": "Email"}
            ),
            "website": TextInput(
                attrs={"class": "form-control", "placeholder": "Website"}
            ),
            "Services": forms.Select(attrs={'class': 'form-control', "placeholder": 'Select Services'}),
        }
