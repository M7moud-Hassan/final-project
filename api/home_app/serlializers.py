from rest_framework import serializers

from authentication.models import Skills
from .models import *

class imageJobSerializer(serializers.ModelSerializer):
    class Meta:
        model = JobImages
        fields = '__all__'

class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = ['name']

class LikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = LikeJob
        fields = '__all__'
class DislikesSerializer(serializers.ModelSerializer):
    class Meta:
        model = DisLike
        fields = '__all__'
class JobSerializer(serializers.ModelSerializer):
    images=imageJobSerializer(read_only=True, many=True)
    skills=SkillsSerializer(read_only=True,many=True)
    likes=LikeSerializer(read_only=True,many=True)
    dislikes=LikeSerializer(read_only=True,many=True)
    class Meta:
        model=Job
        fields = '__all__'
