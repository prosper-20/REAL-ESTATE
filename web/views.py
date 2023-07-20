from django.shortcuts import render
from django.views import View
from api.models import Property

class HomePage(View):
    def get(self, request):
        properties = Property.objects.all()
        context = {
            "properties": properties
        }
        return render(request, "web/index.html", context)



class DetailPage(View):
    def get(self, request, **kwargs):
        slug = kwargs["slug"]

        current_property = Property.objects.get(slug=slug)
        return render(request, "web/propert-detail.html", {"property": current_property})

        
        
