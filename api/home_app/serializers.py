from rest_framework import serializers

from authentication.models import Skills
from profile_app.models import Portflio
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

class NotificationClientSerializer(serializers.ModelSerializer):
    class Meta:
        model = notificationsClient
        fields = '__all__'

class NotificationFreeSerializer(serializers.ModelSerializer):
    class Meta:
        model = notificationsFree
        fields = '__all__'
class ImagesSendApplySerializer(serializers.ModelSerializer):
    class Meta:
        model = ImagesSendApply
        fields = '__all__'

class ApplaySerializer(serializers.ModelSerializer):
    images = ImagesSendApplySerializer(read_only=True, many=True)
    class Meta:
        model = SendApply
        fields = '__all__'
class RegisterUserSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = '__all__'

class RegisterFreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterFreelancer
        fields = ['id','first_name','last_name','user_image','job_title']
class HireSerializer(serializers.ModelSerializer):
    client=RegisterUserSerializer(read_only=True)
    job=JobSerializer(read_only=True)
    free=RegisterFreelancerSerializer(read_only=True)
    class Meta:
        model = Hires
        fields = '__all__'

