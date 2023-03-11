from django.db.models import fields
from rest_framework import serializers

from .models import RegisterFreelancer


class SignUpFreelancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterFreelancer
		fields = ('first_name', 'last_name','email','phone_number','password')

