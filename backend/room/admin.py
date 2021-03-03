from django.contrib import admin
from room.models import (Action, Coach,
                         Game, Player,
                         Set, Team)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('id', 'name', 'uuid')


admin.site.register(Team, TeamAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('number', 'first_name', 'role')


admin.site.register(Player, PlayerAdmin)


class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'is_main')


admin.site.register(Coach, CoachAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('team_name',)


admin.site.register(Game, GameAdmin)


class ActionAdmin(admin.ModelAdmin):
    list_display = ('user', 'set', 'player', )


admin.site.register(Action, ActionAdmin)


class SetAdmin(admin.ModelAdmin):
    list_display = ('team_points', 'opponent_points', 'number', 'game')


admin.site.register(Set, SetAdmin)
