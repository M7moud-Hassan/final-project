from django.shortcuts import render
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from models import CertificationType, Certifications, Portfilo
from profile_app.serlializers import CertificationtypeSerialzer, CertificationsSerialzer


# Create your views here.
@api_view(['GET'])
def get_all_certification_type_serializer(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = CertificationType.objects.filter(**request.query_params.dict())
    else:
        items = CertificationType.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = CertificationtypeSerialzer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_all_certificatins_serializer(request):
    # checking for the parameters from the URL
    if request.query_params:
        items = Certifications.objects.filter(**request.query_params.dict())
    else:
        items = Certifications.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = CertificationsSerialzer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['GET'])
def get_certificatins_using_id_serializer(request, pk):
    items = Certifications.objects.all(id_user_free=pk)

    # if there is something in items else raise error
    if items:
        serializer = CertificationsSerialzer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_portfilo(request):
    item = Portfilo(data=request.data)

    # validating for already existing data
    if Portfilo.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def add_certification (request):
    item = Certifications (data=request.data)

    # validating for already existing data
    if Certifications.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)