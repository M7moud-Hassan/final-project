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

        fields = ('portflio_freelancer','title','description','linkVide')

class PaymentSerialzer(serializers.ModelSerializer):
    class Meta:
        model = Payment
        fields = ['id',
                  'payment_freelancer',
                  'full_name',
                  'street_address',
                  'city',
                  'state',
                  'postal_code',
                  'name_on_card',
                  'credit_card_number',
                  'exp_month',
                  'exp_year',
                  'cvv',]


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

