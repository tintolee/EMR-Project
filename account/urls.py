from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "account"

urlpatterns = [
    path("login/", auth_views.LoginView.as_view(template_name="account/login.html"),name='login'),
    path("logout/", auth_views.LogoutView.as_view(template_name="account/logout.html"), name="logout"),
    path("register/", views.SignUp, name="signup"),
    path("", views.home, name="home"),
    path("aboutus/", views.aboutus, name="about-us"),
    path("contact/", views.contact, name="contact"),
    path("main_dash/", views.main_dash, name="maindash"),
    path("add_patient/", views.add_patient, name="add_patient"),
    path("patients/", views.patients, name="patients"),
    path("patient_details/<int:id>/", views.patient_details, name="patient_details"),
    path("edit_patient/<int:id>/", views.add_patient, name="edit_patient"),
   
]