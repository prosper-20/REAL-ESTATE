from django.db.models.signals import post_save
from .models import User, Profile
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.utils.html import strip_tags
from django.conf import settings

@receiver(post_save, sender=User)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_profile(sender, instance, created, **kwargs):
    instance.profile.save()


@receiver(post_save, sender=User)
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        subject = 'Welcome to Our Website'
        to_email = instance.email
        from_email = settings.DEFAULT_FROM_EMAIL

        # Render email template
        html_message = render_to_string('welcome_email.html', {'user': instance})
        plain_message = strip_tags(html_message)

        # Send the email
        send_mail(subject, plain_message, from_email, [to_email], html_message=html_message)

