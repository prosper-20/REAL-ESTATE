from django.contrib import admin
from .models import City, State, PropertyTpe, Property, Favourite

admin.site.register(Favourite)

@admin.register(City)
class CityAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(State)
class StateAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}


@admin.register(PropertyTpe)
class HomeTypeAdmin(admin.ModelAdmin):
    list_display = ["name", "slug"]
    prepopulated_fields = {'slug': ('name',)}



@admin.register(Property)
class PropertyAdmin(admin.ModelAdmin):
    list_display = ["title", "address", "city", "price", "agent"]
    prepopulated_fields = {'slug': ('title',)}
    list_editable = ["price"]
    search_fields = ["title", "city__name", "agent__username"]
    list_filter = ["type", "agent"]

