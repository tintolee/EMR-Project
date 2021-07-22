from django.contrib.auth import login, logout
from django.urls import reverse_lazy
from django.views.generic import CreateView
from django.shortcuts import redirect, render
from .forms import * 
from user_profile.models import UserProfile
from . models import  Patient, Staff


 #function to add staff
def add_staff(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = StaffForm()
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(instance=staff)
        return render(request, "add_staff.html", {"form": form})
    else:
        if id == 0:
            form = StaffForm(request.POST)
        else:
            staff = Staff.objects.get(pk=id)
            form = StaffForm(request.POST, instance=staff)
        if form.is_valid():
            form.save()
        return redirect('account:staff')

#function to view staff details
def staff_details(request, id):
    staff = Staff.objects.get(pk=id)
    context = {
        "staff": staff
    }
    return render(request, "staff_details.html", context)

def staffs(request):
    staffs = Staff.objects.all()
    return render(request, "staff.html", {"account:staffs": staffs})

def patients(request):
    patients = Patient.objects.all()
    context = {
        "patients": patients
    }
    return render(request, "patients.html", context)


def patient_details(request, id):
    patient = Patient.objects.get(pk=id)
    context = {
        "patient": patient
    }
   
    return render(request, "patient_details.html", context)





def add_patient(request, id=0):
    if request.method == "GET":
        if id == 0:
            form = PatientForm()
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(instance=patient)
        return render(request, "add_patient.html", {"form": form})
    else:
        if id == 0:
            form = PatientForm(request.POST)
        else:
            patient = Patient.objects.get(pk=id)
            form = PatientForm(request.POST, instance=patient)
        if form.is_valid():
            form.save()
        return redirect('account:patients')


def home(request):
    return render(request, 'account/home.html')

#function to view main dashboard by the HR
def main_dash(request):
    return render(request, "maindash.html")

def aboutus(request):
    return render(request, 'account/aboutus.html')

def contact(request):
    return render(request, 'account/contact.html')

def SignUp(request):
    if request.method == 'POST':
        form = UserCreateForm(request.POST)
        if form.is_valid():
            user = form.save()
            first_name = user.first_name
            last_name = user.last_name
            name = first_name + ' ' + last_name
            UserProfile.objects.create(name=name, user=user)
            login(request, user)
            return redirect('account:home')
    else:
        form = UserCreateForm()
    return render(request, 'account/signup.html', {'form': form})



 
    