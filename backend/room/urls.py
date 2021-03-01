from django.urls import path
from room import views


urlpatterns = [
    # path('room/<int:pk>', TeamView.as_view()),
    path('room/', views.teams),
    path('players/', views.players_list),
    path('coaches/', views.coaches_list),
    path('player/<int:pk>', views.player_detail),
]
