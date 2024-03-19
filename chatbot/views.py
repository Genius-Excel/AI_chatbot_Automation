from django.shortcuts import render
from django.http import HttpResponse
from .models import HospitalBookings
from rest_framework import generics
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .serializers import HospitalBookingsSerializer

# Create your views here.
class HospitalCreateAPIView(generics.CreateAPIView):
    queryset = HospitalBookings.objects.all()
    serializer_class = HospitalBookingsSerializer

class AppointmentsAPIView(generics.ListAPIView):
    queryset = HospitalBookings.objects.all()
    serializer_class = HospitalBookingsSerializer

def home(request):
    return render(request, 'home.html')

@api_view(["GET"])
def agatha_marry_me(request):
    return Response("Agatha, this is an API endpoint to prove my love to you! Will you marry me?", status=200)

