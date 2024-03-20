from django.urls import path, include


from . import views


urlpatterns = [
    path("", views.home, name="home"),
    path("login/", views.restaurant_login.as_view(), name="restaurant_login"),
    path("about/", views.about, name="about"),
    path("menu/", views.menu, name="menu"),
    path("bookings/", views.bookings, name="bookings"),
]
