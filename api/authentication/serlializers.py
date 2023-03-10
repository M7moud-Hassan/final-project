from django.db.models import fields
from rest_framework import serializers

from .models import RegistrationFreelancer

class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegistrationFreelancer
		fields = ('name', 'location')

class SignUpFreelancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterFreelancer
		fields = ('first_name', 'last_name','email','phone_number','password')

