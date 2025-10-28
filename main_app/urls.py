from django.urls import path
from .views import Home, ChallengeIndex, ChallengeDetail, UserChallengeIndex

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('challenges/', ChallengeIndex.as_view(), name='challenges_index'),
    path('challenges/<int:challenge_id>/', ChallengeDetail.as_view(), name='challenge_detail'),
    path('userchallenges/', UserChallengeIndex.as_view(), name='user_challenges_index'),
]
