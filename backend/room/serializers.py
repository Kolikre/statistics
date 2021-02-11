from rest_framework import serializers

from room.models import Player, Team
from django.contrib.auth.models import User


class UserSerializers(serializers.ModelSerializer):
    """ Серіалізація користувача """

    class Meta:
        model = User
        fields = (
            'id', 'is_active'
        )


class TeamSerializers(serializers.ModelSerializer):
    """ Серіалізація профіля корстувача """
    user = UserSerializers()

    class Meta:
        model = Team
        fields = (
            'id', 'name', 'create_date', 'league', 'uuid',
            'gender', 'is_active', 'user'
        )


class TeamPostSerializers(serializers.ModelSerializer):
    """ Серіалізація профіля корстувача """

    # user = UserSerializers()
    # players = PlayerPostSerializers(many=True, required=False)

    class Meta:
        model = Team
        fields = (
            'name', 'create_date', 'league', 'gender', 'id'
        )


class PlayerSerializers(serializers.ModelSerializer):
    """ Серіалізація гравця """
    # team_id = TeamSerializers()
    user = UserSerializers()

    class Meta:
        model = Player
        fields = (
            'id', 'number', 'first_name', 'last_name', 'middle_name', 'role',
            'birthday', 'weight', 'height', 'attack', 'block', 'born_at',
            'uuid', 'user', 'team_name', 'team_uuid'
        )


class PlayerPostSerializers(serializers.ModelSerializer):
    """ Серіалізація гравця для POST запиту"""
    # user = UserSerializers()
    # team = TeamSerializers()

    class Meta:
        model = Player
        fields = (
            'number', 'first_name', 'last_name', 'middle_name', 'role',
            'birthday', 'weight', 'height', 'attack', 'block',
            'born_at', 'team_name', 'team_uuid'  #,'team_id'

        )


# class CoachSerializers(serializers.ModelSerializer):
#     """ Серіалізація тренера """
#
#     class Meta:
#         model = Coach
#         fields = (
#             'first_name', 'last_name', 'middle_name', 'born_at', 'birthday',
#             'is_main', 'ia_active', 'user_id'
#         )
