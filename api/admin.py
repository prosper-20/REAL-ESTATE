from django.contrib import admin
from .models import City, State, PropertyTpe, Property

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
    list_display = ["title", "address", "city", "price"]
    prepopulated_fields = {'slug': ('title',)}




# Register your models here.
