from restaurant.models import Booking, Menu
from rest_framework import serializers
from django.contrib.auth.models import User


class BookingSerializer(serializers.ModelSerializer):

    class Meta:
        model = Booking
        fields = "__all__"


class MenuSerializer(serializers.ModelSerializer):

    class Meta:
        model = Menu
        fields = "__all__"
