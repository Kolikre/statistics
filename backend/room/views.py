from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import permissions
from room.models import Team
from room.serializers import TeamSerializers


class TeamView(APIView):
    """ Профіль користувача """

    def get(self, request):
        profile = Team.objects.all()
        serializer = TeamSerializers(profile, many=True)
        return Response({'response': serializer.data})