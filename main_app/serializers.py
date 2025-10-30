from rest_framework import serializers
from .models import Challenge, UserChallenge, Reflection

# ref: cat-collector classwork code

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

class UserChallengeSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    challenge = serializers.PrimaryKeyRelatedField(queryset=Challenge.objects.all())
    class Meta:
        model = UserChallenge
        fields = '__all__'
        read_only_fields = ['user']

class ReflectionSerializer(serializers.ModelSerializer):
    mood_display = serializers.CharField(source='get_mood_display', read_only=True)
    user_challenge_title = serializers.CharField(source='user_challenge.challenge.title', read_only=True)
    class Meta:
        model = Reflection
        fields = '__all__'