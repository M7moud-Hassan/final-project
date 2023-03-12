from django.db.models import fields
from rest_framework import serializers
from .models import RegisterFreelancer , RegisterUser

class SignUpFreelancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterFreelancer
		fields = ('first_name', 'last_name','email','phone_number','password')

class SignUpUserSerialzer(serializers.ModelSerializer):
	class Meta:
		model = RegisterUser
		fields = ('fname', 'lname','email','phone','password')