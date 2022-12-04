from django.urls import path
from . import views

urlpatterns = [
    path('',views.home, name ='home'),
    path('login1/',views.login1, name ='login1'),
    path('signup/',views.signup, name ='signup'),
    path('profile/',views.profile, name ='profile'),
    path('thanks/',views.thanks, name ='thanks'),
]
