from django.db import models

# Create your models here.

class ProfileModel(models.Model):
    full_name = models.CharField(max_length=50)
    email = models.EmailField()
    mobile_no = models.CharField(max_length=20)
    bio = models.TextField(max_length=500)
    course_name = models.CharField(max_length=20)
    course_duration = models.IntegerField()
    course_passout_year = models.IntegerField()
    course_percentage = models.IntegerField()
    company_name = models.CharField(max_length=255)
    duration_of_job = models.IntegerField()
    job_desc = models.TextField(max_length=500)
    sallary = models.IntegerField()
    project_name = models.CharField(max_length=255)
    project_duration =models.IntegerField()
    project_description = models.TextField(max_length=500)
    your_role_in_project = models.TextField(max_length=300)