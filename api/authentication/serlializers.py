from django.db.models import fields
from rest_framework import serializers
<<<<<<< HEAD

from .models import RegisterFreelancer
=======
from .models import RegisterFreelancer , RegisterUser
>>>>>>> 670acac9a8c3f3acaf3fa1a75ededd29389c0c95


class SignUpFreelancerSerializer(serializers.ModelSerializer):
	class Meta:
		model = RegisterFreelancer
		fields = ('first_name', 'last_name','email','phone_number','password')

<<<<<<< HEAD
=======
class SignUpUserSerialzer(serializers.ModelSerializer):
	class Meta:
		model = RegisterUser
		fields = ('fname', 'lname','email','phone','password')
>>>>>>> 670acac9a8c3f3acaf3fa1a75ededd29389c0c95
