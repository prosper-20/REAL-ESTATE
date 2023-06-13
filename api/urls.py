from django.urls import path
from .views import ApiProprtyHomePage


urlpatterns = [
    path("", ApiProprtyHomePage.as_view(), name="api-home")
]