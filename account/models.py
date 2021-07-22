from django.db import models
from django.contrib.auth.models import User, AbstractUser
from django.utils import timezone

# Create your models here.

USER_CHOICES = [
    ('D', 'Doctor'),
    ('P', 'Patient'),
    ('HR', 'HR')
]

SHIFT_CHOICES = (
    ("Day", "Day"),
    ("Night", "Night"),
)

STAFF_CHOICES = (
    ("Doctor", "Doctor"),
    ("Nurse", "Nurse"),
    ("Public Health Officer", "Public Health Officer"),
    ("Cleaner", "Cleaner"),
    ("Security", "Security"),
    ("Driver", "Driver"),
    ("Counselor", "Counselor"),
    ("Nutritionist", "Nutritionist"),
)

class User(AbstractUser):
    user_type = models.CharField(choices=USER_CHOICES, max_length=2)

    def is_doctor(self):
        if self.user_type == 'D':
            return True
        else:
            return False

    def is_patient(self):
        if self.user_type == 'P':
            return True
        else:
            return False

    def is_receptionist(self):
        if self.user_type == 'R':
            return True
        else:
            return False

    def is_HR(self):
        if self.user_type == 'HR':
            return True
        else:
            return False

    class Meta:
        ordering = ('id',)



GENDER_CHOICES = (
    ("Male", "Male"),
    ("Female", "Female"),
)

class BaseInfo(models.Model):
    id_number = models.CharField(max_length=200, unique=True)
    name = models.CharField(max_length=200)   
    gender = models.CharField(max_length=20, choices=GENDER_CHOICES)
    phone = models.CharField(max_length=200)
    email = models.EmailField(max_length=200)
    

    class Meta:
        abstract = True





class Patient(BaseInfo):
    
    
    age=models.IntegerField(null=True, blank=True)
    height=models.IntegerField(null=True, blank=True)
    weight=models.IntegerField(null=True, blank=True)
    ward=models.CharField(max_length=200)
    LGA=models.CharField(max_length=200)
    state=models.CharField(max_length=200)
    date_recorded = models.DateTimeField(default=timezone.now)

    

    def __str__(self):
        return self.name


class Staff(BaseInfo):
    
    position = models.CharField(max_length=100, choices=STAFF_CHOICES)
    employment_date = models.DateTimeField()
    shift = models.CharField(max_length=20, choices=SHIFT_CHOICES)
    
