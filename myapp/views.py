from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from random import randint
from django.core.exceptions import ObjectDoesNotExist
from django.contrib.auth.decorators import login_required
import logging
from django.contrib.auth.hashers import make_password, check_password

logger = logging.getLogger(__name__)

# Create your views here.
def About_Page(request):
    return render(request,'about.html')

def Blog_Single_Page(request):
    return render(request,'blog-single.html')

def Blog_Page(request):
    return render(request,'blog.html')

def Contact_Page(request):
    return render(request,'contact.html')

def Faq_Page(request):
    return render(request,'faq.html')

def Gallery_Page(request):
    return render(request,'gallery.html')

def Index_Page(request):
    return render(request,'index.html')

def Job_Listings_Page(request):
    return render(request,'job-listings.html')

def Job_Single_Page(request):
    return render(request,'job-single.html') 

def Login_Page(request):
    return render(request,'login.html') 

def Portfolio_Single_Page(request):
    return render(request,'portfolio-single.html') 

def Portfolio_Page(request):
    return render(request,'portfolio.html') 

def Post_Job_Page(request):
    return render(request,'post-job.html') 

def Register_Page(request):
    return render(request,'register.html') 

def Service_Single_Page(request):
    return render(request,'service-single.html') 

def Services_Page(request):
    return render(request,'services.html') 

def Testimonials_Page(request):
    return render(request,'testimonials.html') 

def Otp_Verify_Page(request):
    return render(request,'otpverify.html') 



#views 2
def Register_User(request):
    if request.POST['role']=='Candidate':
        role = request.POST['role']
        fname = request.POST['fname']    
        lname = request.POST['lname']    
        email = request.POST['email']    
        password = request.POST['password']    
        cpassword = request.POST['cpassword']    

        user = UserMaster.objects.filter(email=email)

        if user:
            message = "User already exists"
            return render(request,'register.html',{'msg':message})

        else:
            if password == cpassword:
                otp = randint(100000,999999)
                newuser = UserMaster.objects.create(role=role, otp=otp, email=email, password=make_password(password))
                newcand = Candidate.objects.create(user_id=newuser, firstname=fname, lastname=lname)
                return render(request,'otpverify.html', {'email':email})


    else:
        print("Company Registration")
        return render(request,'register.html')

def Otp_Verify(request):
    email = request.POST['email']
    otp = int(request.POST['otp'])

    user = UserMaster.objects.get(email=email)

    if user:
        if user.otp == otp:
            message = "OTP Verification Successful"
            return render(request,'login.html',{'msg':message})
        
        else:
            message = "Invalid OTP"
            return render(request,'otpverify.html',{'msg':message})

    else:
        return render(request,'login.html')  


def Login_User(request):
    if request.POST['role'] == "Candidate":
        email = request.POST['email']
        password = request.POST['password']

        try:
            user = UserMaster.objects.get(email=email)
            
            if check_password(password, user.password) and user.role == "Candidate":
                can = Candidate.objects.get(user_id=user)
                request.session['id'] = user.id
                request.session['role'] = user.role
                request.session['firstname'] = can.firstname
                request.session['lastname'] = can.lastname
                request.session['email'] = user.email
                # Removed password from session for security
                return redirect('index')
            else:
                message = "Invalid credentials"
                return render(request,'login.html',{'msg':message})
        except ObjectDoesNotExist:
            message = "User does not exist"
            return render(request,'login.html',{'msg':message})
    else:
        message = "Invalid role"
        return render(request,'login.html',{'msg':message})

@login_required
def Profile_Page(request, pk):
    if not request.user.is_authenticated:
        return redirect('login')
    user = get_object_or_404(UserMaster, pk=pk)
    can = get_object_or_404(Candidate, user_id=user)
    return render(request, 'profile.html', {'user': user, 'can': can, 'pk': pk})  
    
@login_required
def UpdateProfile(request, pk):
    try:
        user = UserMaster.objects.get(pk=pk)
        if user.role == "Candidate":
            try:
                can = Candidate.objects.get(user_id=user)
                
                # Log the incoming POST data
                logger.debug(f"POST data received: {request.POST}")
                
                # Update candidate fields
                can.firstname = request.POST.get('fname', can.firstname)
                can.lastname = request.POST.get('lastname', can.lastname)
                can.job_type = request.POST.get('job_type', can.job_type)
                can.job_category = request.POST.get('job_category', can.job_category)
                can.city = request.POST.get('city', can.city)
                can.country = request.POST.get('country', can.country)
                can.min_salary = request.POST.get('min_salary', can.min_salary)
                can.max_salary = request.POST.get('max_salary', can.max_salary)
                can.highest_education = request.POST.get('highest_education', can.highest_education)
                can.experience = request.POST.get('experience', can.experience)
                can.website = request.POST.get('website', can.website)
                can.shift = request.POST.get('shift', can.shift)
                can.job_description = request.POST.get('job_description', can.job_description)
                can.contact = request.POST.get('contact', can.contact)
                can.gender = request.POST.get('gender', can.gender)
                
                # Log the candidate object before saving
                logger.debug(f"Candidate object before save: {can.__dict__}")
                
                # Handle file upload
                if 'profile_pic' in request.FILES:
                    can.profile_pic = request.FILES['profile_pic']
                
                # Update user fields
                user.email = request.POST.get('email', user.email)
                
                # Handle password update if provided
                password = request.POST.get('password')
                cpassword = request.POST.get('cpassword')
                
                if password and cpassword:
                    if password == cpassword:
                        user.password = make_password(password)
                    else:
                        message = "Passwords do not match"
                        return render(request, 'profile.html', {'msg': message, 'user': user, 'can': can, 'pk': pk})
                
                try:
                    # Save both objects
                    can.save()
                    user.save()
                    
                    # Log after save
                    logger.debug(f"Candidate object after save: {can.__dict__}")
                    
                    message = "Profile updated successfully"
                    return render(request, 'profile.html', {'msg': message, 'user': user, 'can': can, 'pk': pk})
                except Exception as e:
                    logger.error(f"Error saving profile: {str(e)}")
                    message = f"Error updating profile: {str(e)}"
                    return render(request, 'profile.html', {'msg': message, 'user': user, 'can': can, 'pk': pk})
            except Candidate.DoesNotExist:
                message = "Candidate profile not found"
                return render(request, 'profile.html', {'msg': message, 'user': user, 'pk': pk})
        else:
            message = "Invalid role"
            return render(request, 'profile.html', {'msg': message, 'user': user, 'pk': pk})
    except UserMaster.DoesNotExist:
        message = "User not found"
        return render(request, 'profile.html', {'msg': message, 'pk': pk})


