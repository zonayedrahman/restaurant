from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from .serializers import BookingSerializer, MenuSerializer
from restaurant.models import Booking, Menu
from users.models import User

import requests, jwt


# Create your views here.


# class MenuItemView(generics.ListCreateAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

#     permission_classes = [IsAuthenticated]


class MenuView(APIView):

    def get(self, request):
        token = request.COOKIES.get("jwt")
        # print("token", token)

        if not token:
            return Response({"error": "Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return Response({"error": "Unauthenticated"}, status=401)

        menu = Menu.objects.all()
        serializer = MenuSerializer(menu, many=True)
        return Response(serializer.data)

    def post(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return Response({"error": "Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])

            user_id = payload["id"]

            user = User.objects.get(id=user_id)

            # Would Check if user is a staff member here

        except jwt.ExpiredSignatureError:
            return Response({"error": "Unauthenticated"}, status=401)

        serializer = MenuSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# class SingleMenuItemView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Menu.objects.all()
#     serializer_class = MenuSerializer

#     permission_classes = [IsAuthenticated]


class SingleMenuView(APIView):

    def get(self, request, pk):
        token = request.COOKIES.get("jwt")

        if not token:
            return Response({"error": "Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return Response({"error": "Unauthenticated"}, status=401)

        menu = Menu.objects.get(id=pk)
        serializer = MenuSerializer(menu)
        return Response(serializer.data)


# class BookingView(generics.ListCreateAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

#     permission_classes = [IsAuthenticated]


class BookingView(APIView):

    def get(self, request):
        token = request.COOKIES.get("jwt")

        # print("token", token)

        if not token:
            return Response({"error": "Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return Response({"error": "Unauthenticated"}, status=401)

        booking = Booking.objects.all()
        serializer = BookingSerializer(booking, many=True)
        return Response(serializer.data)

    def post(self, request):
        token = request.COOKIES.get("jwt")

        if not token:
            return Response({"error": "Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])

            user_id = payload["id"]

            user = User.objects.get(id=user_id)

            # Would Check if user is a staff member here

        except jwt.ExpiredSignatureError:
            return Response({"error": "Unauthenticated"}, status=401)

        serializer = BookingSerializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=201)

        return Response(serializer.errors, status=400)


# class SingleBookingView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Booking.objects.all()
#     serializer_class = BookingSerializer

#     permission_classes = [IsAuthenticated]


class SingleBookingView(APIView):

    def get(self, request, pk):
        token = request.COOKIES.get("jwt")

        if not token:
            return Response({"error": "Unauthenticated"}, status=401)

        try:
            payload = jwt.decode(token, "secret", algorithms=["HS256"])

        except jwt.ExpiredSignatureError:
            return Response({"error": "Unauthenticated"}, status=401)

        booking = Booking.objects.get(id=pk)
        serializer = BookingSerializer(booking)
        return Response(serializer.data)
