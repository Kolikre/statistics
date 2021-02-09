from django.urls import path
from room.views import *


urlpatterns = [
    path('room/', TeamView.as_view())
]
