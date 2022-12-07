from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    home_address = models.TextField(max_length=500, null=False, blank=False)
    phone_regex = RegexValidator(
        regex=r'^\+\d{8,15}$', message="Only 15 digits are allowed and the format should be: '+11111111111'."
    )
    phone_number = models.CharField(validators=[phone_regex], max_length=16, null=False, blank=False)
    location_lat = models.DecimalField(max_digits=9, decimal_places=6, null=True)
    location_lon = models.DecimalField(max_digits=9, decimal_places=6, null=True)

@receiver(post_save, sender=User)
def create_user_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)

@receiver(post_save, sender=User)
def save_user_profile(sender, instance, **kwargs):
    instance.profile.save()