from django.urls import path
from .views import AppointmentsAPIView, HospitalCreateAPIView, home

urlpatterns = [
    path('', home, name='home'),
    path('book/', HospitalCreateAPIView.as_view()),
    path('appointments/', AppointmentsAPIView.as_view()),
]