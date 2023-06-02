from django.db import models


class User(models.Model):
    username = models.CharField(max_length=128)
    phone = models.CharField(max_length=15)
    email = models.CharField(max_length=128)
    password = models.CharField(max_length=128)

    first_name = models.CharField(max_length=128)
    middle_name = models.CharField(max_length=128)
    last_name = models.CharField(max_length=128)

    is_staff = models.BooleanField(default=False)
    is_active = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    type = models.SmallIntegerField(default=0)

    def __str__(self):
        return f'{self.username}'


