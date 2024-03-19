from django.urls import path
from .views import AppointmentsAPIView, HospitalCreateAPIView, home, agatha_marry_me

urlpatterns = [
    path('', home, name='home'),
    path('agatha/', agatha_marry_me, name='agatha'),
    path('book/', HospitalCreateAPIView.as_view()),
    path('appointments/', AppointmentsAPIView.as_view()),
]