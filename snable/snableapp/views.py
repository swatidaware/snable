from django.shortcuts import render,redirect
from django.contrib import auth
from django.contrib.auth.models import User
from .models import ProfileModel

# Create your views here.

def home(r):
    return render(r,'snableapp/home.html')

def login1(request):

    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email.lower()).username
        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)

            return redirect('profile')
        else:

            return redirect('login1')
    return render(request, 'accounts/login1.html')

def signup(request):

    if request.method == 'POST':
        firstname = request.POST['firstname']
        lastname = request.POST['lastname']
        username = request.POST['username']
        email = request.POST['email']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']

        if password == confirm_password:
            if User.objects.filter(username=username).exists():

                return redirect('signup')
            else:
                if User.objects.filter(email=email).exists():
                    return redirect('signup')
                else:
                    user = User.objects.create_user(first_name=firstname, last_name=lastname, email=email,
                                                    username=username, password=password)
                    auth.login(request, user)
                    user.save()
                    return redirect('login1')

        else:

            return redirect('signup')
    else:
        return render(request, 'snableapp/signup.html')


def profile(request):
    if request.method == 'POST':
        full_name =request.POST['fullname']
        email =request.POST['email']
        mobile_no =request.POST['mobile']
        bio =request.POST['bio']
        course_name =request.POST['coursename']
        course_duration =request.POST['courseduration']
        course_passout_year =request.POST['passoutyear']
        course_percentage =request.POST['courseparcentage']
        company_name =request.POST['companyname']
        duration_of_job =request.POST['jobduration']
        job_desc =request.POST['jobdesc']
        sallary =request.POST['sallary']
        project_name =request.POST['projectname']
        project_duration =request.POST['projectduration']
        project_description =request.POST['projectdesc']
        your_role_in_project =request.POST['yourrole']

        prof = ProfileModel(full_name=full_name,email=email,mobile_no=mobile_no,bio=bio,course_name=course_name,course_duration=course_duration,
                            course_passout_year=course_passout_year,course_percentage=course_percentage,company_name=company_name,
                            duration_of_job=duration_of_job,job_desc=job_desc,sallary=sallary,project_name=project_name,project_duration=project_duration,
                            project_description=project_description,your_role_in_project=your_role_in_project )
        prof.save()
        return redirect('thanks')

    return render(request,'snableapp/profile.html')


def thanks(r):
    obj = ProfileModel.objects.all()

    return render(r,'snableapp/thanks.html', {'obj':obj})
