from django.contrib import admin
from .models import City, State, PropertyTpe, Property, Favourite, Review, Contact, UploadedImage



admin.site.register(UploadedImage)
# class UploadedImageAdmin(admin.ModelAdmin):
#     list_display = ["get_property_name"]

#     def get_property_name(self, obj):
#         # Define your custom method logic here
#         return obj.property.title

#     get_property_name.short_description = 'house_title'




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



class ReviewAdmin(admin.ModelAdmin):
    list_display = ["user", "property", "rating"]
    search_fields = ["property"]
    list_filter= ["user", "property"]


admin.site.register(Review, ReviewAdmin)


@admin.register(Contact)
class ContactAdmin(admin.ModelAdmin):
    list_display = ["property", "agent", "get_agent_username", "sender", "message"]
    list_filter = ["property", "agent"]

    def get_agent_username(self, obj):
        # Define your custom method logic here
        return obj.agent.username

    get_agent_username.short_description = 'agent_username'

