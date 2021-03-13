from django.urls import path
from room import views


urlpatterns = [
    path('room/', views.teams),
    path('room/<uuid:pk>', views.team),
    path('players/', views.players_list),
    path('player/<uuid:pk>', views.player_detail),
    path('coaches/', views.coaches_list),
    path('coach/<uuid:pk>', views.coach_detail),
    path('games/', views.games),
    path('game/<uuid:pk>', views.game),
]
