from django.db import models

# Create your models here.

class HospitalBookings(models.Model):
    first_name = models.CharField(max_length=250, null=True)
    last_name = models.CharField(max_length=250, null=True)
    email = models.CharField(max_length=250, unique=True, null=True)
    mobile_number = models.CharField(max_length=250, unique=True, null=True)
    doctor_booked = models.CharField(max_length=250, null=True)
    appointment_type = models.CharField(max_length=250, null=True)
    appointment_time = models.DateTimeField(null=True)
    preferred_contact_method = models.CharField(max_length=250, null=True)
    other_appointment_detail = models.CharField(max_length=250, null=True)
    emergency_contact_method = models.CharField(max_length=250, null=True)
    emergency_contact = models.CharField(max_length=250, null=True)
