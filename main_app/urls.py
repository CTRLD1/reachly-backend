from django.urls import path
from .views import Home, ChallengeIndex, ChallengeDetail, UserChallengeIndex, UserChallengeDetail, ReflectionIndex, ReflectionDetail, SignUpUserView, ProfileView, ProgressView

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView

urlpatterns = [
    path('', Home.as_view(), name='home'),
    # Challenge model endpoints
    path('challenges/', ChallengeIndex.as_view(), name='challenges_index'),
    path('challenges/<int:challenge_id>/', ChallengeDetail.as_view(), name='challenge_detail'),
    # UserChallenge model endpoints
    path('userchallenges/', UserChallengeIndex.as_view(), name='user_challenges_index'),
    path('userchallenges/<int:userchallenge_id>/', UserChallengeDetail.as_view(), name='user_challenge_detail'),
    # Reflection model endpoints
    path('reflections/', ReflectionIndex.as_view(), name='reflections_index'),
    path('reflections/<int:reflection_id>/', ReflectionDetail.as_view(), name='reflection_detail'),
    # Auth endpoints
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('signup/', SignUpUserView.as_view(), name='signup'),
    # ProfilePage endpoint
    path('profile/', ProfileView.as_view(), name='profile'),
    # User progress endpoint
    path('progress/', ProgressView.as_view(), name='progress')
     
    
]
