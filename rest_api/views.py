from django.shortcuts import render
from .models.User import User
from rest_framework.decorators import api_view

from .serializers import UserSerializer
from rest_framework.response import Response

@api_view(['GET'])
def user_list(request) :
    users = User.objects.all()
    serializer = UserSerializer(users, many=True)
    return Response(serializer.data)

@api_view(['POST'])
def user_create(request) :
    serializer = UserSerializer(data=request.data)
    if serializer.is_valid(raise_exception=True):
        serializer.save()
        return Response(serializer.data)
