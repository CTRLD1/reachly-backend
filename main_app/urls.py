from django.urls import path
from .views import Home, ChallengeIndex

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('challenges/', ChallengeIndex.as_view(), name='challenges_index'),
]
