from django.contrib.auth.models import AbstractUser
from django.core.validators import validate_email
from django.db import models


class City(models.Model):
    city_name = models.CharField(max_length=200)

    def __str__(self):
        return self.city_name


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True, validators=[validate_email])
    native_city = models.ForeignKey(
        City,
        on_delete=models.CASCADE,
        blank=True,
        null=True
    )

    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = ['username']

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=('email', 'username'),
                name='unique_username_email')
        ]

    def __str__(self):
        return self.email
