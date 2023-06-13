from django.db import models
from users.models import User
import uuid


HOME_TYPE_CHOICES = (
    ("Rent", "Rent"),
    ("Sale", "Sale"),
    ("Lease", "Lease")
)


class City(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Cities"

    def __str__(self):
        return self.name
    

class State(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "States"

    def __str__(self):
        return self.name
    
class PropertyTpe(models.Model):
    name = models.CharField(max_length=100)
    slug = models.SlugField()

    class Meta:
        verbose_name_plural = "Property Types"

    def __str__(self):
        return self.name



class Property(models.Model):
    id = models.UUIDField(primary_key = True, default = uuid.uuid4, editable = False)
    title = models.CharField(max_length=100)
    address = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE)
    state  = models.ForeignKey(State, on_delete=models.CASCADE)
    price = models.DecimalField(max_digits=20, decimal_places=2)
    sale_type = models.CharField(choices=HOME_TYPE_CHOICES, max_length=10)
    type = models.ForeignKey(PropertyTpe, on_delete=models.CASCADE)
    bedrooms = models.IntegerField()
    sqft = models.IntegerField()
    picture = models.ImageField(upload_to="house_images", blank=True, null=True)
    slug = models.SlugField()
    agent = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title
    

