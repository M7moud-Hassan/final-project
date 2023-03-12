from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode, urlsafe_base64_decode
from rest_framework import status
from django.contrib.auth.hashers import make_password, check_password
from .serlializers import *
from .tokens import account_activation_token, Reg_Token
from .models import RegisterFreelancer
from .serlializers import SignUpFreelancerSerializer
from .tokens import account_activation_token
from django.conf import settings
from django.core.mail import send_mail
from rest_framework.response import Response
from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from .token import email_verification_token
from rest_framework.decorators import api_view


@api_view(['POST'])
def signup_freeLancer(request):
    user = SignUpFreelancerSerializer(data=request.data)
    if user.is_valid():
        hashedpassword = make_password(user.data['password'])
        register = RegisterFreelancer.objects.create(first_name=user.data['first_name'],
                                                     last_name=user.data['last_name'], email=user.data['email'],
                                                     password=hashedpassword, phone_number=user.data['phone_number'],
                                                     is_active=False, job_title=None, overview=None, hourly_rate=None,
                                                     user_image=None, street_address=None, city=None,
                                                     state=None, postal_code=None)

        mail_subject = 'Activation link has been sent to your email id'
        messages = "http://current_site.domain/activate?uid=" + str(
            urlsafe_base64_encode(force_bytes(register.id))) + "&token=" + account_activation_token.make_token(register)

        to_email = [user.data['email']]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def registerUserSerialzer(request):
    user = SignUpUserSerialzer(data=request.data)
    if user.is_valid():
        hashPassword = make_password(user.data['password'])
        input = RegisterUser.objects.create(fname=user.data['fname'], lname=user.data['lname'],
                                            email=user.data['email'],
                                            password=hashPassword, phone=user.data['phone'])

        mail_subject = 'Activation link has been sent to your email id'
        messages = "http://current_site.domain/activate?uid=" + str(
            urlsafe_base64_encode(force_bytes(input.id))) + "&token=" + Reg_Token.make_token(input)

        to_email = [user.data['email']]
        from_email = settings.EMAIL_HOST_USER
        send_mail(mail_subject, messages, from_email, to_email)
        return Response(user.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def verify_user_email(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterUser.objects.filter(id=uid).first()
    if user is not None and Reg_Token.check_token(user, request.data['token']):
        user.is_active = True
        user.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def verfy_email(request, token, uid):
    uid = force_str(uid)
    user = RegisterFreelancer.objects.filter(id=uid)
    if user is not None and email_verification_token.check_token(user, token):
        user.is_activate = True
        return Response(user)
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
    # if not user.is_active:
    #     return Response({'error': 'User not activate.'}, status=404)

    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f'http://auth/rest_password/{uid}/{token}/'

    send_mail(
        'Password Reset',
        f'Click the following link to reset your password: {reset_url}',
        'soonfu0@gmail.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'Password reset email sent.'}, status=200)


@api_view(['POST'])
def resetPasswordView(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterFreelancer.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):

        return Response('ok')
    else:

        return Response({'error': 'Invalid password reset token.'}, status=status.HTTP_400_BAD_REQUEST)

        # return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def email_rest_password_user(request):
    email = request.data.get('email')
    if not email:
        return Response({'error': 'Email is required.'}, status=400)

    user = RegisterUser.objects.filter(email=email).first()
    if not user:
        return Response({'error': 'User not found.'}, status=404)

    token = account_activation_token.make_token(user)
    uid = urlsafe_base64_encode(force_bytes(user.pk))
    reset_url = f'http://auth/rest_password_user/{uid}/{token}/'

    send_mail(
        'Password Reset',
        f'Click the following link to reset your password: {reset_url}',
        'soonfu0@gmail.com',
        [email],
        fail_silently=False,
    )

    return Response({'message': 'Password reset email sent.'}, status=200)


@api_view(['POST'])
def rest_password_view_user(request):
    uid = force_str(urlsafe_base64_decode(request.data['uid']))
    user = RegisterUser.objects.filter(id=uid).first()
    if user is not None and account_activation_token.check_token(user, request.data['token']):

        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_service_serializer(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Services.objects.filter(**request.query_params.dict())
    else:
        items = Services.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = ServicesSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def view_skills_serializer(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Skills.objects.filter(**request.query_params.dict())
    else:
        items = Skills.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = SkillsSerializer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
