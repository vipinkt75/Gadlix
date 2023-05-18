# Create your views here.
import json
from django.contrib import messages

from django.http import HttpResponse, JsonResponse
from django.shortcuts import get_object_or_404, render

from .forms import ContactForm
from .models import Client, Gallery, Service, Testimonial, Update


# def index(request):
#     services = Service.objects.all()[:3]
#     gallery1 = Gallery.objects.all().order_by("-id")[0:1]
#     gallery2 = Gallery.objects.all().order_by("-id")[1:2]
#     gallery3 = Gallery.objects.all().order_by("-id")[2:3]
#     gallery4 = Gallery.objects.all().order_by("-id")[3:4]

#     testimonial = Testimonial.objects.all()
#     updates = Update.objects.all()
#     forms = ContactForm(request.POST or None)


#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         context = {
            
#             "form": form,
#         }
#     context = {
#         "is_index": True,
#         "services": services,
#         "gallery1": gallery1,
#         "gallery2": gallery2,
#         "gallery3": gallery3,
#         "gallery4": gallery4,
#         "testimonial": testimonial,
#         "updates": updates,
#         "form": form,
        
        
#     }
#     return render(request, "web/index.html", context)
def index(request):
    services = Service.objects.all()[:3]
    gallery1 = Gallery.objects.all().order_by("-id")[0:1]
    gallery2 = Gallery.objects.all().order_by("-id")[1:2]
    gallery3 = Gallery.objects.all().order_by("-id")[2:3]
    gallery4 = Gallery.objects.all().order_by("-id")[3:4]

    testimonial = Testimonial.objects.all()
    updates = Update.objects.all()
    forms = ContactForm(request.POST or None)

    context = {
        "is_index": True,
        "services": services,
        "gallery1": gallery1,
        "gallery2": gallery2,
        "gallery3": gallery3,
        "gallery4": gallery4,
        "testimonial": testimonial,
        "updates": updates,
        "form": forms,
    }

    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
    else:
        form = ContactForm()

    context['form'] = form

    return render(request, "web/index.html", context)



def about(request):
    testimonial = Testimonial.objects.all()
    context = {"is_about": True, "testimonial": testimonial}
    return render(request, "web/about.html", context)


def services(request):
    services = Service.objects.all()
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    context = {
        "is_service": True,
        "services": services,
        "testimonial": testimonial,
        "client": client,
    }
    return render(request, "web/services.html", context)


def serviceDetails(request, id):
    service = Service.objects.get(id=id)
    # terms=Term.objects.filter(service=service)
    testimonial = Testimonial.objects.all()
    client = Client.objects.all()
    context = {
        "service": service,
        # "terms":terms,
        "testimonial": testimonial,
        "client": client,
    }
    return render(request, "web/service-details.html", context)


def gallery(request):
    gallery = Gallery.objects.all()
    context = {"is_gallery": True, "gallery": gallery}
    return render(request, "web/gallery.html", context)


def blog(request):
    updates = Update.objects.all()
    context = {
        "is_updates": True,
        "updates": updates,
    }
    return render(request, "web/blog.html", context)


def blogDetails(request, slug):
    update = get_object_or_404(Update, slug=slug)
    updates = Update.objects.exclude(pk=update.pk)[:3]
    context = {"update": update, "updates": updates}
    return render(request, "web/blog-details.html", context)


# def contact(request):
#     forms = ContactForm(request.POST or None)
#     context = {"forms": forms}
#     return render(request, "web/contact.html", context)


def ajax(request):
    forms = ContactForm(request.POST or None)
    if request.method == "POST":
        if forms.is_valid():
            forms.save()
            return JsonResponse({"status": True})
        return JsonResponse({"status": False})
# def contact(request):
#     form = ContactForm(request.POST or None)
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
#         context = {
#             "is_contact": True,
#             "form": form,
#         }
#     return render(request, "web/contact.html", context)

# def contact(request):
#     form = ContactForm(request.POST or None)
#     context = {
#         "is_contact": True,
#         "form": form,
#     }
#     if request.method == "POST":
#         if form.is_valid():
#             form.save()
            
#     return render(request, "web/contact.html", context)




def contact(request):
    # Create an instance of the ContactForm, either with POST data or None
    form = ContactForm(request.POST or None)
    if request.method == "POST":
        # If the request method is POST, check if the form data is valid
        if form.is_valid():
            # If the form data is valid, save it to the database
            form.save()
            # Create a JSON response indicating success
            response_data = {
                "status": "true",
                "title": "Successfully Submitted",
                "message": "Message successfully updated",
            }
        else:
            # If the form data is not valid, create a JSON response indicating failure
            print(form.errors)
            response_data = {
                "status": "false",
                "title": "Form validation error",
                "message": "Please correct the errors below and try again.",
            }
        
        # Return a JSON response with the appropriate message
        return HttpResponse(
            json.dumps(response_data), content_type="application/javascript"
        )
    else:
        # If the request method is not POST, render the contact form template with the ContactForm instance
        context = {
            "is_contact": True,
            "form": form,
        }
        return render(request, "web/contact.html", context)