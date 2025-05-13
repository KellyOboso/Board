from myapp.models import UserMaster, Candidate, Company

# Set the username or email of the user you want to delete
USERNAME_OR_EMAIL = 'kellyoboso@gmail.com'

try:
    user = UserMaster.objects.get(username=USERNAME_OR_EMAIL)
except UserMaster.DoesNotExist:
    try:
        user = UserMaster.objects.get(email=USERNAME_OR_EMAIL)
    except UserMaster.DoesNotExist:
        print(f'No user found with username or email: {USERNAME_OR_EMAIL}')
        user = None

if user:
    Candidate.objects.filter(user_id=user).delete()
    Company.objects.filter(user_id=user).delete()
    user.delete()
    print(f'Deleted user and related Candidate/Company for: {USERNAME_OR_EMAIL}') 
    