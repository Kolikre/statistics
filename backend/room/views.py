from rest_framework.parsers import JSONParser
from rest_framework.response import Response
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework import permissions
from room.models import Coach, Team, Player
from room.serializers import (CoachSerializers,  CoachPostSerializers,
                              PlayerPostSerializers, PlayerSerializers,
                              TeamPostSerializers, TeamSerializers)


@api_view(['GET', 'POST'])
def teams(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        snippets = Team.objects.all()
        serializer = TeamSerializers(snippets, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        team_data = TeamPostSerializers(data=request.data)
        profile = Team.objects.filter(user=request.user)
        if team_data.is_valid():
            if profile:
                return Response({"status": "The team is not first"})
            else:
                team_data.save(user=request.user)
            return Response({"status": True})
        else:
            return Response(team_data.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def team(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        team = Team.objects.get(pk=pk)
    except Team.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = TeamSerializers(team)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = TeamPostSerializers(team, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        team.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def players_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        players = Player.objects.filter(user=request.user)
        serializer = PlayerSerializers(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        player_data = PlayerPostSerializers(data=request.data)
        players = Player.objects.filter(user=request.user)
        print(players)
        if len(players) >= 18:  # To do change this value
            return Response({"status": "You have the maximum number of players"})
        else:
            if player_data.is_valid():
                player_data.save(user=request.user)
                return Response({"status": True})
            else:
                return Response(player_data.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def player_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        player = Player.objects.get(pk=pk)
    except Player.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = PlayerSerializers(player)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = PlayerPostSerializers(player, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        player.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def coaches_list(request):
    """
    List all code snippets, or create a new snippet.
    """
    if request.method == 'GET':
        players = Coach.objects.filter(user=request.user)
        serializer = CoachSerializers(players, many=True)
        return Response(serializer.data)

    elif request.method == 'POST':
        coach_data = CoachPostSerializers(data=request.data)
        coaches = Coach.objects.filter(user=request.user)
        print(coaches)
        # if len(coaches) >= 6:  # To do change this value
        #     return Response({"status": "You have the maximum number of coaches"})
        # else:
        if coach_data.is_valid():
            coach_data.save(user=request.user)
            return Response({"status": True})
        else:
            return Response(coach_data.errors)


@api_view(['GET', 'PUT', 'DELETE'])
def coach_detail(request, pk):
    """
    Retrieve, update or delete a code snippet.
    """
    try:
        coach = Coach.objects.get(pk=pk)
    except Coach.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = CoachSerializers(coach)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = CoachPostSerializers(coach, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        coach.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
