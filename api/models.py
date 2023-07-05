from django.db import models
from users.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator


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
    address = models.TextField(blank=True, null=True)
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    state  = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sale_type = models.CharField(choices=HOME_TYPE_CHOICES, max_length=10, blank=True, null=True)
    type = models.ForeignKey(PropertyTpe, on_delete=models.CASCADE, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    sqft = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to="house_images", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)


    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title
    


class Favourite(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ManyToManyField(Property, blank=True)

    def __str__(self):
        return self.user.username
    


class Review(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="reviews")
    rating = models.IntegerField(validators=[MinValueValidator(1), MaxValueValidator(10)])
    comments = models.TextField()

    def __str__(self):
        return self.property.title
    
    
    

