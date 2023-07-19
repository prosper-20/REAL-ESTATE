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
