from django.db import models
from .validators import POSTAL_CODE_VALIDATOR


class Location(models.Model):
    """ Модель описывающая локацию """
    postal_code = models.CharField(
        primary_key=True,
        max_length=6,
        validators=[POSTAL_CODE_VALIDATOR],
        blank=False,
        null=False,
    )
    city = models.CharField(max_length=100, blank=False, null=False)
    state = models.CharField(max_length=100, blank=False, null=False)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=False)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, blank=False, null=False)

    class Meta:
        db_table = 'location'
        indexes = [
            models.Index(fields=['postal_code'])
        ]
