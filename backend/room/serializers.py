from abc import ABC

from rest_framework import serializers

from room.models import Team
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    """ Серіалізація користувача """
    class Meta:
        model = User
        fields = (
            'id',
            'username'
        )


class TeamSerializers(serializers.ModelSerializer):
    """ Серіалізація профіля корстувача """
    user = UserSerializers()

    class Meta:
        model = Team
        fields = (
            'user',
            'name',
            'create_date',
            'uuid',
            'league',
            'gender',
            'is_active'
        )
