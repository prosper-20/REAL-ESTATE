from django.urls import path
from .views import ApiProprtyHomePage, ApiPropertyDetailPage, AddFavouriteProperty, GetFavouriteProperty,SimilarProperty, NewAddFavouriteProperty, AddPropertyReview, PropertyContactView


urlpatterns = [
    path("", ApiProprtyHomePage.as_view(), name="api-home"),
    # path("property/<slug:slug>/<uuid:id>/", ApiPropertyDetailPage.as_view(), name="api-property-detail"),
    path("property/<uuid:id>/", ApiPropertyDetailPage.as_view(), name="api-property-detail"),
    path("property/<uuid:id>/reviews/", AddPropertyReview.as_view(), name="property-review"),
    path("property/<uuid:id>/contact/", PropertyContactView.as_view(), name="property-contact"),
    path("property/<slug:slug>/", ApiPropertyDetailPage.as_view(), name="api-property-detail"),
    path("add-fave/", AddFavouriteProperty.as_view(), name="add-fave"),
    path("property/<slug:slug>/<uuid:id>/add-fave/", NewAddFavouriteProperty.as_view(), name="new-add-fave"),
    path("get-fave/", GetFavouriteProperty.as_view(), name="get-fave"),
    path("property/<slug:slug>/<uuid:id>/similar/", SimilarProperty.as_view(), name="similar")
]