from django.shortcuts import render
# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import User
import requests
from .serializers import UserSerializer

class UserListCreateView(APIView):
    def get(self, request):
        first_name = request.query_params.get('first_name')
        
        if first_name:
            matching_users = User.objects.filter(first_name__istartswith=first_name)
            if matching_users:
                serializer = UserSerializer(matching_users, many=True)
                return Response(serializer.data)
            else:
                response = requests.get(f"https://dummyjson.com/users/search?q={first_name}")
                new_users = response.json()
                created_users = []
                for user_data in new_users:
                    user = User.objects.create(**user_data)
                    created_users.append(user)
                serializer = UserSerializer(created_users, many=True)
                return Response(serializer.data)
        else:
            return Response({"message": "Query parameter 'first_name' is required."}, status=status.HTTP_400_BAD_REQUEST)
