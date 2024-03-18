from django.shortcuts import render
from .models import HospitalBookings
from rest_framework import generics
from .serializers import HospitalBookingsSerializer

# Create your views here.
class HospitalCreateAPIView(generics.CreateAPIView):
    queryset = HospitalBookings.objects.all()
    serializer_class = HospitalBookingsSerializer

class AppointmentsAPIView(generics.ListAPIView):
    queryset = HospitalBookings.objects.all()
    serializer_class = HospitalBookingsSerializer

