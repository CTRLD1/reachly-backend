from rest_framework import serializers
from .models import Challenge, UserChallenge, Reflection

# ref: cat-collector classwork code

class ChallengeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Challenge
        fields = '__all__'

class UserChallengeSerializer(serializers.ModelSerializer):
    status_display = serializers.CharField(source='get_status_display', read_only=True)
    challenge = serializers.StringRelatedField()
    class Meta:
        model = UserChallenge
        fields = '__all__'

class ReflectionSerializer(serializers.ModelSerializer):
    mood_display = serializers.CharField(source='get_mood_display', read_only=True)
    challenge_title = serializers.CharField(source='challenge.title', read_only=True)
    class Meta:
        model = Reflection
        fields = '__all__'