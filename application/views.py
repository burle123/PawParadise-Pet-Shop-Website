from django.shortcuts import redirect, render, get_object_or_404
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from application.models import enquiry_table

from django.views.decorators.csrf import csrf_exempt
from django.views.decorators.csrf import csrf_protect

from django.http import JsonResponse
import json
# Create your views here.

def home(request):
    
    return render(request, 'index.html')

def about(request):
    
    return render(request, 'about.html')

def contact(request):
    if request.method == "POST":
        a = request.POST.get('name')
        b = request.POST.get('email')
        c = request.POST.get('phone')
        d = request.POST.get('message')
        enquiry = enquiry_table(name = a, email = b, phone = c, message = d)
        enquiry.save()

        messages.success(request, 'Enquiry Form Submitted Successfully...')
        
    return render(request, 'contact.html')
    
def services(request):
    
    return render(request, 'services.html')

def store(request):
    
    return render(request, 'store.html')

def blog(request):
    
    return render(request, 'blog.html')

def index(request):
    
    return render(request, 'index.html')

def blogdetails1(request):
    
    return render(request, 'blog-details.html')

def blogdetails2(request):
    
    return render(request, 'blog-details2.html')

def blogdetails3(request):
    
    return render(request, 'blog-details3.html')

def blogdetails4(request):
    
    return render(request, 'blog-details4.html')

def blogdetails5(request):
    
    return render(request, 'blog-details5.html')

def blogdetails6(request):
    
    return render(request, 'blog-details6.html')

def dashboard(request):
    
    return render(request, 'dashboard/dashboard.html')

