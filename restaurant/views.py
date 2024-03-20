import datetime
from django.shortcuts import render, redirect
from django.views import View
from rest_framework.response import Response

from .forms import LoginForm

import jwt, requests

# Create your views here.


def home(request):
    return render(request, "restaurant/home.html")


def about(request):
    return render(request, "restaurant/about.html")


class restaurant_login(View):
    form_class = LoginForm

    def get(self, request):
        form = self.form_class()

        return render(request, "restaurant/login.html", {"form": form})



def menu(request):

    # Get the token from the cookie
    token = request.COOKIES.get("jwt")

    print("TOKEN: ", token)

    # If token not present, redirect to login
    if not token:
        # print("NO TOKEN")
        alert = "You need to login to view the menu."
        return redirect("restaurant_login")

    # If token present, send to the API
    response = requests.get(
        "http://localhost:8000/api/restaurant/menu/",
        cookies={"jwt": token},
    )

    # print("RESPONSE: ", response.json(), response.status_code)

    print(datetime.datetime.now())

    if response.status_code == 200:
        return render(request, "restaurant/menu.html", {"menu": response.json()})

    else:
        # print("here")
        alert = "You need to login to view the menu."
        return redirect("restaurant_login")


def bookings(request):

    # Get the token from the cookie
    token = request.COOKIES.get("jwt")

    # If token not present, redirect to login
    if not token:
        # print("NO TOKEN")
        alert = "You need to login to view the menu."
        return redirect("restaurant_login")

    # If token present, send to the API

    response = requests.get(
        "http://localhost:8000/api/restaurant/bookings/",
        cookies={"jwt": token},
    )

    # print("RESPONSE: ", response.json())

    context = {}

    bookings = response.json()

    for booking in bookings:
        booking["booking_date"] = (
            f'{booking["booking_date"].split("T")[0]} {booking["booking_date"].split("T")[1][:8]}'
        )

    context["bookings"] = bookings

    return render(request, "restaurant/bookings.html", context)
