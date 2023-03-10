from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode,urlsafe_base64_decode
from rest_framework import status
from rest_framework.decorators import api_view
# Create your views here.
from django.contrib.auth.hashers import make_password ,check_password
from django.core.mail import EmailMessage

from .models import RegisterFreelancer
from .serlializers import SignUpFreelancerSerializer
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from django.utils.encoding import force_str
from django.shortcuts import get_object_or_404

@api_view(['POST'])
def signup_freeLancer(request):
    user = SignUpFreelancerSerializer(data=request.data)
    if user.is_valid():
        hashedpassword = make_password(user.data['password'])
        register=RegisterFreelancer.objects.create(first_name=user.data['first_name'],
                                         last_name=user.data['last_name'],email=user.data['email'],
                                         password=hashedpassword,phone_number=user.data['phone_number'],
                                          is_active=False)


        mail_subject = 'Activation link has been sent to your email id'
        messages ="http://current_site.domain/activate?uid="+str(urlsafe_base64_encode(force_bytes(register.id)))+"&token="+account_activation_token.make_token(register)


        to_email = [user.data['email']]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def verfy_email(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterFreelancer.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):
        user.is_active=True
        user.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
@api_view(['POST'])
def emailResetPassword(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required.'}, status=400)

    user = RegisterFreelancer.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'User not found.'}, status=404)

    token = account_activation_token._make_hash_value(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f'localhost://reset_password/<uidb64>/<token>//{uid}/{token}/'

    send_mail(
        'Password Reset',
        f'Click the following link to reset your password: {reset_url}',
        'soonfu0@gmail.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'Password reset email sent.'}, status=200)


@api_view(['GET'])
def resetPasswordView(request, uidb64, token):
    try:
        uid = force_str(urlsafe_base64_decode(uidb64))
        user = get_object_or_404(RegisterFreelancer, id=uid)
    except (TypeError, ValueError, OverflowError, RegisterFreelancer.DoesNotExist):
        user = None

    if user is not None and account_activation_token._make_hash_value().check_token(user, token):
        return Response({'uid': uid}, status=status.HTTP_200_OK)
    else:
        return Response({'error': 'Invalid password reset token.'}, status=status.HTTP_400_BAD_REQUEST)

