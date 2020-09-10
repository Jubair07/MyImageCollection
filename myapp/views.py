from django.shortcuts import render
from django.http import HttpResponse
from myapp.models import *
from datetime import datetime
from django.contrib import messages
from myapp.models import Image

# Create your views here.\
def home(request):
    cats = Category.objects.all()
    images = Image.objects.all()
    data = {'images':images, 'cats':cats}

    return render(request,'a.html', data)

def show_category(request, cid):
    cats = Category.objects.all()

    category=Category.objects.get(pk=cid)


    images = Image.objects.filter(cat=category)
    data = {'images':images, 'cats':cats}

    return render(request,'a.html', data)

def contact(request):
    if request.method == "POST":
        name = request.POST.get('name')
        email= request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        contact = Contact(name=name, email=email, phone=phone, desc=desc, date= datetime.today())
        contact.save()
        messages.success(request, 'Your message has been sent!')
        

    return render(request,'contact.html')

def search(request):
    #allImages = Image.objects.all()
    query = request.GET['query']
    allImages = Image.objects.filter(title__icontains=query)
    params = {'allImages':allImages}
    return render(request,'search.html',params)
    #return HttpResponse("This is search ")
