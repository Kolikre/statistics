from rest_framework import serializers

from room.models import Coach, Game, Player, Team
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
            'name', 'create_date', 'league', 'uuid',
            'gender', 'is_active', 'user'
        )


class TeamPostSerializers(serializers.ModelSerializer):
    """ Серіалізація профіля корстувача """

    class Meta:
        model = Team
        fields = (
            'name', 'create_date', 'league', 'gender'
        )


class PlayerSerializers(serializers.ModelSerializer):
    """ Серіалізація гравця """
    # team_id = TeamSerializers()
    user = UserSerializers()

    class Meta:
        model = Player
        fields = "__all__"
        #     (
        #     'id', 'number', 'first_name', 'last_name', 'middle_name', 'role',
        #     'birthday', 'weight', 'height', 'attack', 'block', 'born_at',
        #     'uuid', 'user', 'team_name', 'team_uuid', 'is_active'
        # )


class PlayerPostSerializers(serializers.ModelSerializer):
    """ Серіалізація гравця для POST запиту"""

    class Meta:
        model = Player
        fields = (
            'number', 'first_name', 'last_name', 'middle_name', 'role',
            'birthday', 'weight', 'height', 'attack', 'block',
            'born_at', 'team_name', 'team_uuid', 'is_active',
            'is_cap', 'zone', 'negative_attack', 'negative_block',
            'negative_set', 'negative_serve', 'negative_dig', 'negative_rc',
            'positive_attack', 'positive_block', 'positive_set', 'positive_serve',
            'positive_dig', 'positive_rc', 'total_attack', 'total_block',
            'total_set', 'total_serve', 'total_dig', 'total_rc', 'index_attack',
            'index_block', 'index_set', 'index_serve', 'index_dig', 'index_block'

        )


class CoachSerializers(serializers.ModelSerializer):
    """ Серіалізація тренера """
    # team_id = TeamSerializers()
    user = UserSerializers()

    class Meta:
        model = Coach
        fields = (
            'first_name', 'last_name', 'middle_name',
            'birthday', 'born_at', 'phone',
            'uuid', 'user', 'team_name', 'team_uuid', 'is_active'
        )


class CoachPostSerializers(serializers.ModelSerializer):
    """ Серіалізація тренера для POST запиту  """

    class Meta:
        model = Coach
        fields = (
            'first_name', 'last_name', 'middle_name',
            'birthday', 'born_at', 'phone',
            'team_name', 'team_uuid', 'is_active'
        )


class GameSerializers(serializers.ModelSerializer):
    """ Серіалізація гри """

    user = UserSerializers()
    # players = PlayerSerializers()

    class Meta:
        model = Game
        fields = "__all__"


class GamePostSerializers(serializers.ModelSerializer):
    """ Серіалізація гри """

    class Meta:
        model = Game
        fields = ('team_name', 'opponent_name', 'set_number',
                  'team_points', 'opponent_points', 'player_name',
                  'player_uuid', 'action', 'action_time')
