from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import render
from .models.User import User
from .serializers import UserSerializer

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
        #return Response(serializer.data)
        return Response(status=status.HTTP_200_OK)
    return Response(status=status.HTTP_500_INTERNAL_SERVER_ERROR)