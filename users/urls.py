from django.urls import path
from .views import ApiUserRegistrationView, ConfirmEmailView

urlpatterns = [
    path("register/", ApiUserRegistrationView.as_view(), name="register"),
    path('confirm-email/<uidb64>/<str:token>/', ConfirmEmailView.as_view(), name='confirm-email'),
]