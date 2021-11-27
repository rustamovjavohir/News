from django.contrib.auth.models import User
from django.db import models

# Create your models here.
from news.models import Uploads


class Employee(models.Model):
    phone = models.CharField(max_length=14)
    profile_picture = models.OneToOneField(Uploads, on_delete=models.CASCADE)
    auth_user = models.OneToOneField(User, on_delete=models.CASCADE)

    class Meta:
        db_table = 'auth_employee'


class VerifyToken(models.Model):
    token = models.CharField(max_length=100, unique=True)
    auth_user = models.ForeignKey(User, on_delete=models.CASCADE, default=1)
    deleted = models.IntegerField(default=0)

    class Meta:
        db_table = 'verify_token'
