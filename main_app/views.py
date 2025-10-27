from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Challenge
from .serializers import ChallengeSerializer

# Create your views here.

# just to test the API
class Home(APIView):
    def get(self, request):
        content = {'message': 'helloo welcome to reachly API🙋🏽'}
        return Response(content)
    
# Challenge model (full CRUD)
class ChallengeIndex(APIView):
    def get(self, request):
        try:
            # to get all of the challenges from the db
            queryset = Challenge.objects.all()
            serializer = ChallengeSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # CREATE 
    def post(self, request):
        try:
            serializer = ChallengeSerializer(data=request.data)

            # if its valid, save it and return a HTTP 201 CREATED status as a response
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        