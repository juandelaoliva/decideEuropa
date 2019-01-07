from django.db import models
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError

# Create your models here

class UserDecide(models.Model):
    first_name = models.CharField(max_length = 30)
    last_name = models.CharField(max_length = 30)
    email = models.EmailField(unique = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE)

class TwoStepsAuth(models.Model):
    code = models.CharField(max_length = 192, unique = True)
    user = models.OneToOneField(User, on_delete = models.CASCADE, unique = True)

class UserStatus(models.Model):
    status = models.CharField(max_length = 192)
    user = models.OneToOneField(User, on_delete = models.CASCADE, unique = True)

    def clean(self):
        status_collection = ['LOCKED', 'ACTIVE', 'RECENTLY_REGISTERED']
        if not self.status in status_collection:
            raise ValidationError(_("The user's status is invalid"),
                code = 'user_status_invalid')
    
