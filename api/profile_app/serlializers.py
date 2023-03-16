from rest_framework import serializers

from .models import *

class ImagesProjectSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(required=False)
    class Meta:
        model=ImagesProject
        fields = ['image']

class CertificationsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class CertificationtypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CertificationType
        fields = '__all__'

class portfiloSerialzer(serializers.ModelSerializer):
    images = ImagesProjectSerializer(many=True,read_only=True)
    class Meta:
        model = Portflio
        fields = ['title','portflio_freelancer','linkVide','description','images']