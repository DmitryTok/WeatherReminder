from django.core.validators import MinValueValidator
from django.db import models
from django.utils import timezone

from users.models import City, CustomUser


class Period(models.Model):
    period = models.PositiveIntegerField(validators=[MinValueValidator(1)], default=6)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return str(self.period)


class Measurement(models.Model):
    measure = models.CharField(max_length=50, unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.measure


class SubType(models.Model):
    sub_type = models.CharField(max_length=70, unique=True)

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return self.sub_type


class Subscription(models.Model):
    user = models.ForeignKey(
        CustomUser,
        on_delete=models.CASCADE
    )
    city = models.ForeignKey(
        City,
        on_delete=models.CASCADE
    )
    period = models.ForeignKey(
        Period,
        on_delete=models.CASCADE
    )
    measure = models.ForeignKey(
        Measurement,
        on_delete=models.CASCADE
    )
    subscription_date = models.DateTimeField(default=timezone.now)
    type_subscription = models.ForeignKey(
        SubType,
        on_delete=models.CASCADE
    )

    class Meta:
        ordering = ('id',)

    def __str__(self):
        return f'{self.user} {self.type_subscription}'
