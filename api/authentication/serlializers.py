from rest_framework import serializers
from .models import CertificationType,Certifications, RegisterFreelancer, RegisterUser, CategoryService, Services, Skills,Certifications, Portfilo





class ServicesSerializer(serializers.ModelSerializer):

    class Meta:
        model = Services
        fields = '__all__'


class CategoryServiceSerializer(serializers.ModelSerializer):
    services = ServicesSerializer(many=True, read_only=True)
    service_nams = serializers.CharField(source="ServicesSerializer.name", read_only=True)
    class Meta:
        model = CategoryService
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


class CertificationsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Certifications
        fields = '__all__'

class CertificationtypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CertificationType
        fields = '__all__'

class portfiloSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Portfilo
        fields = '__all__'




