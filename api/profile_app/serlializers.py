from rest_framework import serializers

from .models import Certification, CertificationType, Portflio


class CertificationsSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Certification
        fields = '__all__'

class CertificationtypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CertificationType
        fields = '__all__'

class portfiloSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Portflio
        fields = '__all__'