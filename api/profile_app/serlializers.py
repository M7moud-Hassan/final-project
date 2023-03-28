from rest_framework import serializers

from authentication.models import Experience
from home_app.models import ReviewAndRate
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


class History_workSerialzer(serializers.ModelSerializer):
    class Meta:
        model = WorkHistory
        fields = '__all__'

class EmploymentHistorySerialzer(serializers.ModelSerializer):
    class Meta:
        model = Employment_History
        fields = '__all__'


class CertificationsTypeSerialzer(serializers.ModelSerializer):
    class Meta:
        model = CertificationType
        fields = ['name']

class CertificationsSerialzer(serializers.ModelSerializer):
    certification_type = CertificationsTypeSerialzer()
    class Meta:
        model = Certification
        fields = '__all__'

class ExperiencesSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Experience
        fields = '__all__'

class PaymentFreeMethodSerial(serializers.ModelSerializer):
    class Meta:
        model = PaymentFreeMethod
        fields = '__all__'

class PaymentMethodSerial(serializers.ModelSerializer):
    class Meta:
        model = PaymentMethod
        fields = '__all__'
class RegisterSerial(serializers.ModelSerializer):
    class Meta:
        model = RegisterUser
        fields = ['id','fname','lname','image']
class ReviewAndRateSerial(serializers.ModelSerializer):
    client=RegisterSerial(read_only=True)
    class Meta:
        model = ReviewAndRate
        fields = '__all__'