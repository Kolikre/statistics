from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework.generics import get_object_or_404
from rest_framework.views import APIView
from rest_framework import permissions
from room.models import Team, Player
from room.serializers import (PlayerPostSerializers, PlayerSerializers,
                              TeamPostSerializers, TeamSerializers)


class TeamView(APIView):
    """ User profile """

    permission_classes = [permissions.IsAuthenticated]

    def get(self, request):
        profile = Team.objects.filter(user=request.user)
        serializer = TeamSerializers(profile, many=True)
        return Response({"response": serializer.data})

    def post(self, request):
        team_data = TeamPostSerializers(data=request.data)
        profile = Team.objects.filter(user=request.user)

        if team_data.is_valid():
            if profile:
                return Response({"status": "The team is not first"})
            else:
                team_data.save(user=request.user)
            return Response(team_data.data)
        else:
            return Response(team_data.errors)


class PlayerView(APIView):
    """ Player  """

    # parser_classes = [JSONParser]
    permission_classes = [permissions.IsAuthenticated]
    # permission_classes = [permissions.AllowAny]

    def get(self, request):
        player_profile = Player.objects.filter(user=request.user)
        serializer = PlayerSerializers(player_profile, many=True)
        return Response({"response": serializer.data})

    def post(self, request):
        player_data = PlayerPostSerializers(data=request.data)

        if player_data.is_valid():
            player_data.save(user=request.user)
            return Response(player_data.data)
        else:
            return Response(player_data.errors)


# class CoachView(APIView):
#     """ Coach """
#
#     def get(self, request):
#         coaches = Coach.object.filter(user=request.user)
#         serializer = CoachSerializers(coaches, data=request.data)
#         return Response({"response": serializer.data})
