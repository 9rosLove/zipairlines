from rest_framework import serializers

from airplanes.models import Airplane
from user.models import User
from user.serializers import UserSerializer


class AirplaneSerializer(serializers.ModelSerializer):
    class Meta:
        model = Airplane
        fields = (
            "id",
            "airplane_id",
            "passengers_count",
            "fuel_tank_capacity_in_liters",
            "fuel_consumption_per_minute",
            "maximum_flight_time_in_minutes",
        )


class UserPostSerializer(UserSerializer):
    full_name = serializers.CharField(source="__str__", read_only=True)

    class Meta:
        model = User
        fields = ("id", "full_name", "email")


class AirplaneDetailSerializer(serializers.ModelSerializer):
    created_by = serializers.SerializerMethodField()
    fuel_tank_capacity_in_liters = serializers.FloatField()
    fuel_consumption_per_minute = serializers.FloatField()
    maximum_flight_time_in_minutes = serializers.FloatField()

    class Meta:
        model = Airplane
        fields = "__all__"

    def get_created_by(self, instance):
        if instance.created_by:
            return UserPostSerializer(instance.created_by).data
        return None
