from django.db import models
from django.contrib.auth.models import User

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    credits= models.IntegerField(default=20)
    last_reset = models.DateTimeField(auto_now_add=True)



