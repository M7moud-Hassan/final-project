import base64

from django.contrib.auth.hashers import check_password, make_password
from rest_framework import status, serializers
from rest_framework.decorators import api_view
from rest_framework.response import Response

from home_app.models import ReviewAndRate
from .models import *
from .serlializers import *
from authentication.models import RegisterFreelancer, Skills, Services, Experience, Education

from authentication.models import RegisterUser


# Create your views here.@api_view(['GET'])
@api_view(['GET'])
def get_all_certification_type_serializer(request):
    items = CertificationType.objects.all()
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
        return Response(serializer.data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def details_freelancer(request):
    id=request.data['id']
    user=RegisterFreelancer.objects.filter(id=id).first()
    if user:
        image_data = base64.b64encode(user.user_image.read()).decode('utf-8')
        educations=user.education.all()
        list_ed=[]
        for ed in educations:
            list_ed.append({
                "id":ed.id,
                 "school":ed.school,
                "from_year":ed.from_year
            })
        list_exp=[]
        experiences=user.experience.all()
        for exp in experiences:
            list_exp.append({
                "id":exp.id,
                "title": exp.title,
                "company": exp.company,
                "description": exp.description
            })
        skills=user.skills.all()
        myskills=[]
        for sk in skills:
            myskills.append(sk.name)
        myServeces=[]
        services=user.services.all()
        for se in services:
            myServeces.append(se.name)

        history_work=WorkHistory.objects.filter(work_history_freelancer=user)
        portfilos_list=[]
        portfilos=Portflio.objects.filter(portflio_freelancer=user)
        for p in portfilos:
            portfilos_list.append({
                "id":p.id,
                "date_time":p.date_time,
                "title":p.title,
                "linkvideo":p.linkVide,
                "description":p.description,
                "image":base64.b64encode(p.images.first().image.read()).decode('utf-8')
            })
        certification = Certification.objects.filter(certification_user_freelancer=user)
        employmentHistorys=Employment_History.objects.filter(id_free=user)
        numRate=0
        reviews=ReviewAndRate.objects.filter(free=user)
        for r in reviews:
            numRate+=r.rate
        rate=numRate/len(reviews)
        return  Response({
            "numReview":len(reviews),
            "rate":rate,
            "reviews":ReviewAndRateSerial(reviews,many=True).data,
            "name":f'{user.first_name} {user.last_name}',
            "address":user.city,
            "jobtitle": user.job_title,
            "overView":user.overview,
            "image":image_data,
            "educations":list_ed,
            "skills":myskills,
            "experiecnces":list_exp,
            "services":myServeces,
            "history_work":History_workSerialzer(history_work,many=True).data,
            "portfilos":portfilos_list if portfilos_list else [],
            "certifications":CertificationsSerialzer(certification,many=True).data,
            "empolumentHistory":EmploymentHistorySerialzer(employmentHistorys,many=True).data
        })
    else:
        return Response('not found')



@api_view(['POST'])
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
    portflio=None
    if user:
        if (request.data['date_time'] == '0000-00-00'):
            portflio = Portflio.objects.create(
                portflio_freelancer=user,
                title=request.data['title']
                , linkVide=request.data['linkVide'],
                description=request.data['description'],)
        else:
            portflio = Portflio.objects.create(
                portflio_freelancer=user,
                title=request.data['title']
                , linkVide=request.data['linkVide'],
                description=request.data['description'],
                date_time=request.data['date_time'])
        for f in request.FILES.getlist('images[]'):
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
        return Response(CertificationsSerialzer(certificate).data)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)


@api_view(['POST'])
def add_history_work(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        WorkHistory.objects.create(work_history_freelancer=user,
                                   location=request.data['location'],
                                   date=request.data['date'],
                                   cost=request.data['cost'])
        return Response('ok')
    else:
        Response('not fount free')

@api_view(['POST'])
def add_history_employment(request):
    print(request.data['id'])
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        emp= Employment_History.objects.create(
            company=request.data['company'],
                                         location=request.data['location'],
                                         title=request.data['title'],
                                         period_from_month=request.data['period_from_month'],
                                         period_to_month=request.data['period_to_month'],
                                         is_current_work=request.data['is_current_work'],
                                         description=request.data['description'],
                                            id_free=user)
        return Response(EmploymentHistorySerialzer(emp).data)
    else:
        Response('not fount free')

@api_view(['POST'])
def clientDetails(request):
    id=request.data['id']
    user=RegisterUser.objects.filter(id=id).first()
    if user:
        fname = user.fname
        lname = user.lname
        phone = user.phone
        email = user.email
        image = ''
        if user.image:
            image = base64.b64encode(user.image.read()).decode('utf-8')
        history_work = WorkHistory.objects.filter(work_history_client=user)
        return  Response({
            "name":f'{fname} {lname}',
            "phone":phone,
            "email": email,
            "image":image,
            "fname":fname,
            "lname":lname,
            "street":user.street,
            "city":user.city,
            "state":user.state,
            "history_work":History_workSerialzer(history_work,many=True).data,
            "postal_code":user.postal_code,
            "is_payments":True if PaymentMethod.objects.filter(client_id=id) else False
        })
    else:
        return Response('not found')



@api_view(['POST'])
def updateSkills(request):

    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:

        user.skills.set([])
        user.save()
        for sk in request.data['skills']:
            user.skills.add(Skills.objects.filter(id=sk['value']).first())
        user.save()
        return  Response('ok')
    else:
        return Response("not found")

@api_view(['POST'])
def updateServices(request):
    user = RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        user.services.set([])
        user.save()
        for sk in request.data['services']:
            user.services.add(Services.objects.filter(id=sk['value']).first())
        user.save()
        return Response('ok')
    else:
        return Response("not found")
@api_view(['POST'])
def delete_experience(request):
   result= Experience.objects.filter(id=request.data['exp_id']).first()
   user= RegisterFreelancer.objects.filter(id=request.data['id']).first()
   if user:
       user.experience.remove(result)
       ob={
           "id": result.id,
           "title": result.title,
           "company": result.company,
           "description": result.description
       }
       result.delete()
       return  Response(ob)
   else:
       return  Response('not found')
@api_view(['POST'])
def getExperience(request):
    exp = Experience.objects.filter(id=request.data['id']).first()
    if exp:
        return Response({'exp':ExperiencesSerialzer(exp).data})
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)

@api_view(['POST'])
def secondaryDetails(request):
    id=request.data['id']
    user=RegisterUser.objects.filter(id=id).first()
    if user:
        user.street=request.data['street']
        user.city=request.data['city']
        user.state=request.data['state']
        user.postal_code=request.data['postal_code']
        user.phone=request.data['phone']
        user.fname=request.data['fName']
        user.lname=request.data['lName']
        user.save()
        return  Response('ok')
    else:
        return Response('not added')
@api_view(['POST'])
def updateImageUser(request):

    user=RegisterUser.objects.filter(id=request.data['id']).first()
    if user:
        user.image=request.data['image']
        user.save()
        return Response('ok')
    else:
        return Response('not found')

@api_view(['POST'])
def FreeDetails(request):
    id=request.data['id']
    user=RegisterFreelancer.objects.filter(id=id).first()
    if user:
        first_name = user.first_name
        last_name = user.last_name
        phone_number = user.phone_number
        email = user.email
        user_image = ''
        if user.user_image:
            user_image = base64.b64encode(user.user_image.read()).decode('utf-8')
        return  Response({
            "name":f'{first_name} {last_name}',
            "phone_number":phone_number,
            "email": email,
            "user_image":user_image,
            "first_name":first_name,
            "last_name":last_name,
            "street_address":user.street_address,
            "city":user.city,
            "state":user.state,
            "postal_code":user.postal_code
        })
    else:
        return Response('not found')
@api_view(['POST'])
def secondaryDetailsFree(request):
    id=request.data['id']
    user=RegisterFreelancer.objects.filter(id=id).first()
    if user:
        user.street_address=request.data['street_address']
        user.city=request.data['city']
        user.state=request.data['state']
        user.postal_code=request.data['postal_code']
        user.phone_number=request.data['phone_number']
        user.first_name=request.data['first_name']
        user.last_name=request.data['last_name']
        user.save()
        return Response('ok')
    else:
        return Response('not added')
@api_view(['POST'])
def updateImageFreeUser(request):
    user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
    if user:
        user.user_image=request.data['user_image']
        user.save()
        return Response('ok')
@api_view(['POST'])
def delEducation(request):
    ed=Education.objects.filter(id=request.data['id']).first()
    if ed:
        obj={
                    "id":ed.id,
                     "school":ed.school,
                    "from_year":ed.from_year
                }
        ed.delete()
        return Response(obj)

    else:
        return Response('not found')
@api_view(['POST'])
def PaymentFreelanceUser(request):
    free_id=request.data['free_id']
    user =RegisterFreelancer.objects.filter(id=free_id).first()
    print(user)
    if user:
        PaymentFreeMethod.objects.create(
        nameOnTheCard= request.data['nameOnTheCard'],
        email = request.data['email'],
        state = request.data['state'],
        city = request.data['city'],
        Zip_code = request.data['Zip_code'],
        Expire_year = request.data['Expire_year'],
        Expire_month = request.data['Expire_month'],
        Credit_number = request.data['Credit_number'],
        CVV = request.data['CVV'],
        free_id=user
        )
        return Response('ok')
    else:
        return Response('not added')


@api_view(['POST'])
def PaymentUser(request):
    client_id=request.data['client_id']
    user =RegisterUser.objects.filter(id=client_id).first()
    print(user)
    if user:
        PaymentMethod.objects.create(
        nameOnTheCard= request.data['nameOnTheCard'],
        email = request.data['email'],
        state = request.data['state'],
        city = request.data['city'],
        Zip_code = request.data['Zip_code'],
        Expire_year = request.data['Expire_year'],
        Expire_month = request.data['Expire_month'],
        Credit_number = request.data['Credit_number'],
        CVV = request.data['CVV'],
        client_id=user
        )
        return Response('ok')
    else:
        return Response('not added')



@api_view(['POST'])

def delPortFilo(request):
    p=Portflio.objects.filter(id=request.data['id']).first()
    if p:
        p.delete()
        return  Response('ok')
    else:
        return Response('not found')
@api_view(['POST'])
def delcertificate(request):
    c=Certification.objects.filter(id=request.data['id']).first()
    if c:
        c.delete()
        return Response('ok')
    else:
        return Response('not found')
@api_view(['POST'])
def delHistoryEmpl(request):
    h=Employment_History.objects.filter(id=request.data['id']).first()
    if h:
        h.delete()
        return Response('ok')
    else:
        return Response('not found')
@api_view(['POST'])
def changePasswordFreelancer(request):
        user=RegisterFreelancer.objects.filter(id=request.data['id']).first()
        print(user)
        password = request.data['password']
        if user:
            if check_password(password, user.password):
                user.password=make_password(request.data['newPassword'])
                user.save()
                return Response('ok')
            else:
                return Response('wrong password')
@api_view(['POST'])
def changePassword(request):
        print(request.data)
        user=RegisterUser.objects.filter(id=request.data['id']).first()
        print(user)
        password = request.data['password']
        if user:
            if check_password(password, user.password):
                user.password=make_password(request.data['newPassword'])
                user.save()
                return Response('ok')
            else:
                return Response('wrong password')


@api_view(['POST'])
def FreePaymentCards(request):
    free_id = request.data['free_id']
    print(free_id)
    cards = PaymentFreeMethod.objects.filter(free_id=free_id)
    print(cards)
    if cards:
        return Response(PaymentFreeMethodSerial(
            cards,many=True
        ).data)
    else:
        return Response({'message': 'not found'})
@api_view(['POST'])
def clientPaymentCards(request):
    client_id = request.data['client_id']
    print(client_id)
    cards = PaymentMethod.objects.filter(client_id=client_id)
    print(cards)
    if cards:
        return Response(PaymentMethodSerial(
            cards,many=True
        ).data)
    else:
        return Response({'message': 'not found'})

