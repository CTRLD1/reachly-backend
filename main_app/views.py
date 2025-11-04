from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Challenge, UserChallenge, Reflection
from .serializers import ChallengeSerializer, UserChallengeSerializer, ReflectionSerializer
from django.shortcuts import get_object_or_404

from rest_framework.permissions import AllowAny, IsAuthenticated, IsAuthenticatedOrReadOnly
from django.contrib.auth import get_user_model

# Create your views here.

# just to test the API
class Home(APIView):
    def get(self, request):
        content = {'message': 'helloo welcome to reachly API🙋🏽'}
        return Response(content)
    
# Challenge model (full CRUD)
class ChallengeIndex(APIView):
    permission_classes = [AllowAny]
    def get(self, request):
        try:
            # to get all of the challenges from the db
            queryset = Challenge.objects.all()
            serializer = ChallengeSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # CREATE a new challenge
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
    permission_classes = [AllowAny]
    # READ a single challenge by Id
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
        
    
# UserChallenge model (partial CRUD)    
class UserChallengeIndex(APIView):
    permission_classes = [IsAuthenticated]
    # to get the user's challenges info 
    def get(self, request):
        try:
            queryset = UserChallenge.objects.filter(user=request.user)
            serializer = UserChallengeSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # CREATE: so the user can add a new challenge from the available challenges in the db
    def post(self, request):
        try:
            serializer = UserChallengeSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


class UserChallengeDetail(APIView):
    permission_classes = [IsAuthenticated]
    # READ a single user challenge by Id
    def get(self, request, userchallenge_id):
        try:
            queryset = get_object_or_404(UserChallenge, id=userchallenge_id, user=request.user)
            serializer =   UserChallengeSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)

        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # UPDATE  
    def patch(self, request, userchallenge_id):
        try:
            queryset = get_object_or_404(UserChallenge, id=userchallenge_id, user=request.user)
            serializer = UserChallengeSerializer(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_200_OK) 
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
            

   
# Reflection model (full CRUD)
class ReflectionIndex(APIView):
    permission_classes = [IsAuthenticated]
    def get(self, request):
        try:
            # to get the reflections of the user from the db
            queryset = Reflection.objects.filter(user=request.user)
            serializer = ReflectionSerializer(queryset, many=True)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # CREATE a new reflection
    def post(self, request):
        try:
            serializer = ReflectionSerializer(data=request.data)

            # if its valid, save it and return a HTTP 201 CREATED status as a response
            if serializer.is_valid():
                serializer.save(user=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        

class ReflectionDetail(APIView):
    permission_classes = [IsAuthenticated]
    # READ a single reflection by Id
    def get(self, request, reflection_id):
        try:
            queryset = get_object_or_404(Reflection, id=reflection_id, user=request.user)
            serializer = ReflectionSerializer(queryset)
            return Response(serializer.data, status=status.HTTP_200_OK)
        
        except Exception as err:
             return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # UPDATE 
    def patch(self, request, reflection_id):
        try:
            queryset = get_object_or_404(Reflection, id=reflection_id)
            serializer = ReflectionSerializer(queryset, data=request.data, partial=True)
            if serializer.is_valid():
                serializer.save()
                return Response(serializer.data, status=status.HTTP_200_OK)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        except Exception as err:
            return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
        
    # DELETE
    def delete(self, request, reflection_id):
        try:
            queryset = get_object_or_404(Reflection, id=reflection_id)
            queryset.delete()
            return Response({'message:' f'Reflection {reflection_id} has been deleted successfully'}, status=status.HTTP_204_NO_CONTENT)
        
        except Exception as err:
                return Response({'error' : str(err)}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)


# Auth
User = get_user_model()

# Signup new user
# ref: cat-collector backend classwork code

class SignUpUserView(APIView):
    permission_classes = [AllowAny]

    def post(self, request):
        # to get username, email, password directly from request and it will be saved in user variable, same with email
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')
        first_name = request.data.get('first_name')
        last_name = request.data.get('last_name')

        if not username or not password:
            return Response(
                {'error': 'please provide a username, password, and email'},
                status=status.HTTP_400_BAD_REQUEST,
                )
        
        if User.objects.filter(username=username).exists():
            return Response({'error' : 'User Already Exists'},
            status=status.HTTP_400_BAD_REQUEST,               
            )

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
            first_name=first_name,
            last_name=last_name,
            
        )
        return Response({
            'id': user.id,
            'username': user.username,
            'email': user.email,
            'first_name' : user.first_name,
            'last_name': user.last_name,

        }, status=status.HTTP_201_CREATED)
    
    
# to delte a user  
class DeleteUser(APIView):
    permission_classes = [IsAuthenticated]
    
    def delete(self, request):
        user = request.user
        username=user.username
        user.delete()
        return Response(
            {'message' : f'User {username} has been deleted successfully'}
        )
    
    
# get user's profile info for ProfilePage 
class ProfileView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        return Response({
            'id': user.id,
            'username' : user.username,
            'email' : user.email,
            'first_name' : user.first_name,
            'last_name': user.last_name,
        })


class ProgressView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        user = request.user
        total = UserChallenge.objects.filter(user=user).count()
        pending = UserChallenge.objects.filter(user=user, status='P').count()
        in_progress = UserChallenge.objects.filter(user=user, status='IP').count()
        completed = UserChallenge.objects.filter(user=user, status='C').count()

        return Response({
            'total' : total,
            'pending' : pending,
            'in_progress' : in_progress,
            'completed' : completed,
        })

