from django.urls import path
from room import views


urlpatterns = [
    # path('room/<int:pk>', TeamView.as_view()),
    path('room/', views.teams),
    path('room/<int:pk>', views.team),
    path('players/', views.players_list),
    path('player/<int:pk>', views.player_detail),
    path('coaches/', views.coaches_list),
    path('coach/<int:pk>', views.coach_detail),
]
