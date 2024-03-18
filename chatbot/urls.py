from django.urls import path
from .views import AppointmentsAPIView, HospitalCreateAPIView

urlpatterns = [
    path('book/', HospitalCreateAPIView.as_view()),
    path('appointments/', AppointmentsAPIView.as_view()),
]