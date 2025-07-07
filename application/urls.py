"""project2 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,include
from application import views
from django.conf import settings
from django.conf.urls.static import static  

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('aboutus/', views.about, name='about'),
    path('contactus/', views.contact, name='contact'),
    path('Services/', views.services, name='services'),
    path('Store/', views.store, name='store'),
    path('Blog/', views.blog, name='blog'),
    path('Home/', views.index, name='index'),
    path('Dogs/', views.blogdetails1, name='blogdetails1'),
    path('Cats/', views.blogdetails2, name='blogdetails2'),
    path('Birds/', views.blogdetails3, name='blogdetails3'),
    path('Fishs/', views.blogdetails4, name='blogdetails4'),
    path('Rabbits/', views.blogdetails5, name='blogdetails5'),
    path('Rats/', views.blogdetails6, name='blogdetails6'),
    path('Dashboard/', views.dashboard, name='dashboard'),

  

]
