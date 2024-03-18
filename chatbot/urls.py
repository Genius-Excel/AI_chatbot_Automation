from django.urls import path
from .views import HospitalCreateAPIView

urlpatterns = [
    path('book/', HospitalCreateAPIView.as_view())
]