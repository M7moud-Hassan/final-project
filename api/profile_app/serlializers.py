from rest_framework import serializers

from .models import Certification, CertificationType, Portflio, Payment


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
