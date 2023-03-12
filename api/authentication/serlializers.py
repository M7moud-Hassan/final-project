from django.db.models import fields
from rest_framework import serializers

from .models import RegisterFreelancer, RegisterUser, CategoryService, Services, Skills


class CategoryServiceSerializer(serializers.ModelSerializer):


    class Meta:
        model = CategoryService
        fields = '__all__'


class ServicesSerializer(serializers.ModelSerializer):
    services = CategoryServiceSerializer(many=True, read_only=True)
    service_nams = serializers.CharField(source="CategoryService.name", read_only=True)
    class Meta:
        model = Services
        fields = '__all__'


class SkillsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Skills
        fields = '__all__'


class SignUpFreelancerSerializer(serializers.ModelSerializer):
    class Meta:
        model = RegisterFreelancer
        fields = ('first_name', 'last_name', 'email', 'phone_number', 'password')


class SignUpUserSerialzer(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ('fname', 'lname', 'email', 'phone', 'password')
