from django.urls import path
from .views import ApiProprtyHomePage, ApiPropertyDetailPage


urlpatterns = [
    path("", ApiProprtyHomePage.as_view(), name="api-home"),
    path("property/<slug:slug>/<uuid:id>/", ApiPropertyDetailPage.as_view(), name="api-property-detail")
]