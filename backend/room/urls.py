from django.urls import path
from room.views import *


urlpatterns = [
    path('room/<int:pk>', TeamView.as_view()),
    path('room/', TeamView.as_view()),
    path('players/', PlayerView.as_view()),
   #  path('coaches/', CoachView())
]
