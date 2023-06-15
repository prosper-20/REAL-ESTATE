from django.urls import path
from .views import ApiUserRegistrationView

urlpatterns = [
    path("register/", ApiUserRegistrationView.as_view(), name="register")
]