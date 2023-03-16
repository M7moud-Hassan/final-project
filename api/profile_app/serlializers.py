from rest_framework import serializers

from models import Certifications, CertificationType, Portfilo


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