from django.db.models import fields
from rest_framework import serializers
from .models import RegistrationFreelancer

class PublisherSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegistrationFreelancer
		fields = ('name', 'location')