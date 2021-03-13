from django.contrib import admin
from room.models import (Coach,
                         Game, Player,
                         Team)


class TeamAdmin(admin.ModelAdmin):
    list_display = ('name', 'uuid')


admin.site.register(Team, TeamAdmin)


class PlayerAdmin(admin.ModelAdmin):
    list_display = ('number', 'first_name', 'role')


admin.site.register(Player, PlayerAdmin)


class CoachAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'is_main')


admin.site.register(Coach, CoachAdmin)


class GameAdmin(admin.ModelAdmin):
    list_display = ('team_name', 'opponent_name')


admin.site.register(Game, GameAdmin)
