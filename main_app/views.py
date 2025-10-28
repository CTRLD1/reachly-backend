from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Challenge, UserChallenge
from .serializers import ChallengeSerializer, UserChallengeSerializer
from django.shortcuts import get_object_or_404

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


class ChallengeDetail(APIView):
    # READ
    def get(self, request, challenge_id):
        try:
            queryset = get_object_or_404(Challenge, id=challenge_id)
            serializer = ChallengeSerializer(queryset)
            return Response(serializer.data)
        
        except Exception as err:
             return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # UPDATE
    def put(self, request, challenge_id):
        try:
            queryset = get_object_or_404(Challenge, id=challenge_id)
            serializer = ChallengeSerializer(queryset, data=request.data)
            
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
                return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


    # DELETE
    def delete(self, request, challenge_id):
        try:
            queryset = get_object_or_404(Challenge, id=challenge_id)
            queryset.delete()
            return Response({'message:' f'Challenge {challenge_id} has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as err:
                return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    
    
class UserChallengeIndex(APIView):
    def get(self, request):
        try:
            queryset = UserChallenge.objects.all()
            serializer = UserChallengeSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        


    # TODO
    # partial CRUD for UserChallenge model (GET, POST, PUT)
    # full CRUD for Refletion model 
    