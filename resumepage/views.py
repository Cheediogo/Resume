from django.shortcuts import render
from .models import Contact
from django.http import HttpResponse
# Create your views here.


def homepage(request):
    if request.method == "POST":
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        message = request.POST.get('message')
        contact = Contact.objects.create(email=email,message=message,phone=phone)
        contact.save()
        if contact:
            return HttpResponse('Message sent successfully')
        else:
            return HttpResponse("Your message wasnt sent successfuly")
    return render(request,'home.html')