from rest_framework import serializers
from hotels.models import Rooms,Reservations

class RoomsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms
        fields = '__all__'

class ReservationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Reservations
        fields = ['guest_fullname', 'guest_email', 'arrival_date', 'departure_date', 'adults', 'children']

class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rooms,Reservations
        fields = ("name", "username", "email", "password","passwordConfirm")