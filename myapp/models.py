from django.db import models

# Create your models here.
class UserMaster(models.Model):
    email = models.EmailField(max_length=50)
    password = models.CharField(max_length=50)
    otp = models.IntegerField()
    role = models.CharField(max_length=50)
    is_active = models.BooleanField(default=False)
    is_verified = models.BooleanField(default=False)
    is_created = models.DateTimeField(auto_now_add=True)
    is_updated = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.email

class Candidate(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE) 
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    address = models.CharField(max_length=150)    
    dob = models.CharField(max_length=50)
    gender = models.CharField(max_length=50)
    min_salary = models.BigIntegerField(null=True, blank=True)
    max_salary = models.BigIntegerField(null=True, blank=True)
    job_type = models.CharField(max_length=150)
    job_category = models.CharField(max_length=150)
    country = models.CharField(max_length=150)
    highest_education = models.CharField(max_length=150)
    experience = models.CharField(max_length=150)
    website = models.CharField(max_length=150)
    shift = models.CharField(max_length=150)
    job_description = models.CharField(max_length=150)
    profile_pic = models.ImageField(upload_to="static/images")

    def __str__(self):
        return self.firstname

class Company(models.Model):
    user_id = models.ForeignKey(UserMaster,on_delete=models.CASCADE)
    firstname = models.CharField(max_length=50)
    lastname = models.CharField(max_length=50)
    company_name = models.CharField(max_length=50)
    state = models.CharField(max_length=50)
    city = models.CharField(max_length=50)
    contact = models.CharField(max_length=50)
    adress = models.CharField(max_length=150)
    logo_pic = models.ImageField(upload_to="static/images")  

    def __str__(self):
        return self.firstname  

