from django.http import HttpResponse
from django.shortcuts import render


def home(request):
    # return HttpResponse("Hello , you are on ouer home page")
    return render(request , 'website/index.html')

def about(request):
    # return HttpResponse("Hello , you are on ouer About page")
    return render(request , 'website/about.html')

def contact(request):
    # return HttpResponse("Hello , you are on ouer contact page")
    return render(request , 'website/contact.html')