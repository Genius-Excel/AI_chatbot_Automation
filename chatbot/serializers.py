from rest_framework import serializers 
from .models import HospitalBookings

class HospitalBookingsSerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalBookings
        fields = "__all__"