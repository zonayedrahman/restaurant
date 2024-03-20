from django.urls import path


from .views import *


urlpatterns = [
    path("menu/", MenuView.as_view(), name="menu"),
    path("menu/<int:pk>/", SingleMenuView.as_view(), name="single_menu"),
    path("bookings/", BookingView.as_view(), name="booking"),
    path("bookings/<int:pk>/", SingleBookingView.as_view(), name="single_booking"),
]
