from django.db import models
from users.models import User



HOME_TYPE_CHOICES = (
    ("Rent", "Rent"),
    ("Sale", "Sale"),
    ("Lease", "Lease")
)


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    

class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name
    
class HomeType(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    def __str__(self):
        return self.name



class Property(models.Model):
    title = models.CharField(max_length=100)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state  = models.ForeignKey(State, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_type = models.CharField(choices=HOME_TYPE_CHOICES, max_length=10)
    home_type = models.ForeignKey(HomeType, on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    sqft = models.IntegerField()
    picture = models.ImageField(upload_to="house_images", blank=True, null=True)
    slug = models.SlugField()
    agent = models.ForeignKey(User, on_delete=models.CASCADE)


