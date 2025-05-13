"""
URL configuration for myproject project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.2/topics/http/urls/
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
from django.urls import path
from . import views

urlpatterns = [
    path('about/', views.About_Page, name='about'),
    path('blog_single/', views.Blog_Single_Page, name='blog_single'),
    path('blog/', views.Blog_Page, name='blog'),
    path('contact/', views.Contact_Page, name='contact'),
    path('faq/', views.Faq_Page, name='faq'),
    path('gallery/', views.Gallery_Page, name='gallery'),
    path('', views.Index_Page, name='index'),
    path('job_listings/', views.Job_Listings_Page, name='job_listings'),
    path('job_single/', views.Job_Single_Page, name='job_single'),
    path('login/', views.Login_Page, name='login'),
    path('porfolio_single/', views.Portfolio_Single_Page, name='portfolio_single'),
    path('portfolio/', views.Portfolio_Page, name='portfolio'),
    path('post_job/', views.Post_Job_Page, name='post_job'),
    path('register/', views.Register_Page, name='register'),
    path('service_single/', views.Service_Single_Page, name='service_single'),
    path('services/', views.Services_Page, name='services'),
    path('testimonials/', views.Testimonials_Page, name='testimonials'),
    path('otpverify/', views.Otp_Verify_Page, name='otpverify'),
    path('profile/<int:pk>/', views.Profile_Page, name='profile'),
    
    #views' urls
    path('registeruser/', views.Register_User, name='registeruser'),
    path('loginuser/', views.Login_User, name='loginuser'),
    path('otp/',views.Otp_Verify, name='otp'),
    path('updateprofile/<int:pk>/', views.UpdateProfile, name='updateprofile')
]
