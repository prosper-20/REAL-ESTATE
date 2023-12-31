from django.urls import path
from .views import ApiUserRegistrationView, ConfirmEmailView, ApiAgentRegistrationView

urlpatterns = [
    path("register/", ApiUserRegistrationView.as_view(), name="register"),
    path("register/agent/", ApiAgentRegistrationView.as_view(), name="register-agent"),
    path('confirm-email/<uidb64>/<str:token>/', ConfirmEmailView.as_view(), name='confirm-email'),
]