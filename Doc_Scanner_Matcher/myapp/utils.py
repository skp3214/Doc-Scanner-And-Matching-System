from django.utils import timezone
from .models import UserProfile
def reset_credits():
    now = timezone.now()
    today_midnight = timezone.datetime.combine(now.date(), timezone.datetime.min.time(), tzinfo=now.tzinfo)

    profiles = UserProfile.objects.all()
    for profile in profiles:
        if profile.last_reset.date() < now.date():
            profile.credits = 20
            profile.last_reset = today_midnight  
            profile.save()
