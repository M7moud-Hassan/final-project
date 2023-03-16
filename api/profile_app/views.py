from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response


from .models import *
from .serlializers import *



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
        items = Certification.objects.filter(**request.query_params.dict())
    else:
       items = Certification.objects.all()

    # if there is something in items else raise error
    if items:
        serializer = CertificationsSerialzer(items, many=True)
     #   return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['GET'])
def details_freelancer(request):
    id=request.data['id']
    user=RegisterFreelancer.objects.fliter(id=id).first()
    if user:
        title = models.CharField(max_length=50)
        company = models.CharField(max_length=100)
        location = models.CharField(max_length=200)
        is_current_work_in_company = models.BooleanField(default=False)
        start_date = models.DateField()
        end_date = models.DateField()
        description = models.CharField(max_length=500)
        id = models.AutoField
        return  Response({
            "name":"mahmoud hassan",
            "address":"sohage",
            "jobtitle":"software ",
            "overView":"dkdhdhhdhddhhd",
            "educations":[
                {
                    "school":"school",
                    "from_year":"to_year"
                },
                {
                    "school": "school",
                    "from_year": "to_year"
                },

            ]
            ,
            "skills":[
                "sksjjs",
                "sjsjjsj",
                "sjksjjsjs"
            ],
            "experiecnces":[
                {
                    "title":"title",
                    "company":"djhdjjhd",
                    "description":"djdhdjhjdjdjd",
                },
                {
                    "title": "title",
                    "company": "djhdjjhd",
                    "description": "djdhdjhjdjdjd",
                }
            ]

        })
    else:
        return Response('not found')


@api_view(['GET'])
def get_Portfilo_using_id_serializer(request):
    items = Portflio.objects.all(id_user_free=request.data['id'])

    # if there is something in items else raise error
    if items:
        serializer = portfiloSerialzer(items, many=True)
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def add_portflio(request):
    item = Portflio(data=request.data)

    # validating for already existing data
    if Portflio.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)



@api_view(['POST'])
def add_certification (request):
    item = Certification (data=request.data)

    # validating for already existing data
    if Certification.objects.filter(**request.data).exists():
        raise serializers.ValidationError('This data already exists')

    if item.is_valid():
        item.save()
        return Response(item.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)