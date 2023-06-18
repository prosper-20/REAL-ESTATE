from django.urls import path
from .views import ApiProprtyHomePage, ApiPropertyDetailPage, AddFavouriteProperty, GetFavouriteProperty


urlpatterns = [
    path("", ApiProprtyHomePage.as_view(), name="api-home"),
    path("property/<slug:slug>/<uuid:id>/", ApiPropertyDetailPage.as_view(), name="api-property-detail"),
    path("add-fave/", AddFavouriteProperty.as_view(), name="add-fave"),
    path("get-fave/", GetFavouriteProperty.as_view(), name="get-fave")
]