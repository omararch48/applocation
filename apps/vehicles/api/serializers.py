from rest_framework import serializers
from apps.vehicles.models import Vehicle
from apps.users.api.serializers import UserSerializer


class VehicleSerializer(serializers.ModelSerializer):
    user = UserSerializer()

    class Meta:
        model = Vehicle
        fields = ['id', 'user', 'plates', 'last_position',]
