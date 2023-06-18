from django.urls import path
from .views import ApiProprtyHomePage, ApiPropertyDetailPage, AddFavouriteProperty, GetFavouriteProperty,SimilarProperty


urlpatterns = [
    path("", ApiProprtyHomePage.as_view(), name="api-home"),
    path("property/<slug:slug>/<uuid:id>/", ApiPropertyDetailPage.as_view(), name="api-property-detail"),
    path("add-fave/", AddFavouriteProperty.as_view(), name="add-fave"),
    path("get-fave/", GetFavouriteProperty.as_view(), name="get-fave"),
    path("property/<slug:slug>/<uuid:id>/similar/", SimilarProperty.as_view(), name="similar")
]