from django.contrib import admin
from room.models import Team


class TeamAdmin(admin.ModelAdmin):

    list_display = ('user', 'name', 'uuid')


admin.site.register(Team, TeamAdmin)
