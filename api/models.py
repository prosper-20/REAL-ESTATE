from django.db import models
from users.models import User
import uuid
from django.core.validators import MinValueValidator, MaxValueValidator
from django.urls import reverse
from PIL import Image

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
    description = models.TextField()
    features = models.TextField()
    city = models.ForeignKey(City, on_delete=models.CASCADE, blank=True, null=True)
    state  = models.ForeignKey(State, on_delete=models.CASCADE, blank=True, null=True)
    price = models.DecimalField(max_digits=20, decimal_places=0, blank=True, null=True)
    sale_type = models.CharField(choices=HOME_TYPE_CHOICES, max_length=10, blank=True, null=True)
    type = models.ForeignKey(PropertyTpe, on_delete=models.CASCADE, blank=True, null=True)
    bedrooms = models.IntegerField(blank=True, null=True)
    bathrooms = models.IntegerField(blank=True, null=True)
    sqft = models.IntegerField(blank=True, null=True)
    picture = models.ImageField(upload_to="house_images", blank=True, null=True)
    slug = models.SlugField(blank=True, null=True)
    agent = models.ForeignKey(User, on_delete=models.CASCADE)

    def get_absolute_url(self):
        return reverse("detail", kwargs={"slug": self.slug})


    @property
    def image_url(self):
        if self.picture and hasattr(self.picture, 'url'):
            return self.picture.url


    class Meta:
        verbose_name_plural = "Properties"

    def __str__(self):
        return self.title
    
# This is for the image resizing 

class UploadedImage(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE)
    original_image = models.ImageField(upload_to='house_uploads/')
    thumbnail_image = models.ImageField(upload_to='house_uploads/thumbnails/', blank=True)
    medium_image = models.ImageField(upload_to='house_uploads/medium/', blank=True)
    large_image = models.ImageField(upload_to='house_uploads/large/', blank=True)


    def save(self, *args, **kwargs):
        super(UploadedImage, self).save(*args, **kwargs)

        if self.original_image:
            # Open the original image
            original_image = Image.open(self.original_image.path)

            # Resize the image to create the thumbnail version
            thumbnail_size = (100, 100)
            thumbnail_image = original_image.copy()
            thumbnail_image.thumbnail(thumbnail_size)
            thumbnail_image.save(self.thumbnail_image.path)

            # Resize the image to create the medium version
            medium_size = (500, 500)
            medium_image = original_image.copy()
            medium_image.thumbnail(medium_size)
            medium_image.save(self.medium_image.path)

            # Resize the image to create the large version
            large_size = (800, 800)
            large_image = original_image.copy()
            large_image.thumbnail(large_size)
            large_image.save(self.large_image.path)
    


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
    

class Contact(models.Model):
    property = models.ForeignKey(Property, on_delete=models.CASCADE, related_name="contact_property")
    agent = models.ForeignKey(User, on_delete=models.CASCADE, related_name="property_agent")
    sender = models.CharField(max_length=100)
    message = models.TextField()

    def __str__(self):
        return self.sender
    
    
    

