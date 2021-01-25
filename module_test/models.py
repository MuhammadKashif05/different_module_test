from django.contrib.auth.models import User
from django.db import models
import reversion


reversion.register(User)


@reversion.register
class ClientProfile(models.Model):
    user = models.OneToOneField(User, related_name='client_profile', on_delete=models.CASCADE)
    name = models.CharField(max_length=128, null=True, blank=True)
    phone = models.CharField(max_length=128, null=True, blank=True)
    updated_at = models.DateTimeField(auto_now=True)

