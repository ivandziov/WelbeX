from django.db import models
from common.validators import validate_range
from location.models import Location


class Cargo(models.Model):
    pick_up_location = models.ForeignKey(Location,
                                         on_delete=models.DO_NOTHING,
                                         blank=False,
                                         null=False,
                                         related_name='pick_up',
                                         )
    delivery_location = models.ForeignKey(Location,
                                          on_delete=models.DO_NOTHING,
                                          blank=False,
                                          null=False,
                                          related_name='delivery',
                                          )
    weight = models.PositiveIntegerField(validators=[validate_range(1, 1000)])
    description = models.CharField(max_length=1000, blank=True, null=True)

    class Meta:
        db_table = 'cargo'
