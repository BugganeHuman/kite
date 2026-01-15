from django.urls import path, include
from .views import signup, home
urlpatterns = [
    path("", home, name="home"),
    path("accounts/", include("django.contrib.auth.urls")),
    path("accounts/signup", signup, name="signup"),
]