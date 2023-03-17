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
    user =RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        portflio=Portflio.objects.create(portflio_freelancer=user,title=request.data['title']
                          ,linkVide=request.data['linkVide'],
                          description=request.data['linkVide'])
        for f in request.FILES.getlist('images'):
            imageProject = ImagesProject.objects.create(image=f)
            portflio.images.add(imageProject)

        portflio.save()
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)




@api_view(['POST'])
def add_certification (request):
    user = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    certificate_type=CertificationType.objects.filter(id=request.data['type_certificate']).first()
    if user and certificate_type:
        certificate=Certification.objects.create(certification_user_freelancer=user,
                                  provider=request.data['provider'],
                                  description=request.data['description'],
                                  issuse_date=request.data['issuse_date'],
                                  expiration_date=request.data['expiration_date'],
                                  certification_ID=request.data['certification_ID'],
                                  certification_UR=request.data['certification_UR'],
                                  certification_type=certificate_type)
        return Response('ok')
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)