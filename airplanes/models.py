from math import log

from django.db import models

from zipairlines import settings


class Airplane(models.Model):
    airplane_id = models.PositiveSmallIntegerField()
    passengers_count = models.PositiveSmallIntegerField()
    created_by = models.ForeignKey(
        settings.AUTH_USER_MODEL, on_delete=models.SET_NULL, null=True
    )
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def fuel_tank_capacity_in_liters(self):
        return self.airplane_id * 200

    def fuel_consumption_per_minute(self):
        base_fuel_consumption = log(self.airplane_id) * 0.8
        additional_fuel_consumption = self.passengers_count * 0.002
        fuel_consumption = base_fuel_consumption + additional_fuel_consumption

        return fuel_consumption

    def maximum_flight_time_in_minutes(self):
        return self.fuel_tank_capacity_in_liters() / self.fuel_consumption_per_minute()
