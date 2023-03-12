from django.shortcuts import render

# Create your views here.
@api_view(['post'])
def login(request):
    email= request.data['email']
    password=request.data['password']
    hash_password=make_password(password)
    user_free=RegisterFreelancer.objects.filter(email=email,password=hash_password).first()
    if user_free:
        if user_free.is_active:
            return Response({"freeLancer": user_free.id})
        else:
            return Response({"freeLancer": 'not active'})
    else:
        user_free=RegisterUser.objects.filter(email=email,password=hash_password).second()
        if user_free:
            if user_free.is_active:
                return Response({"user": user_free.id})
            else:
                return Response({"freeLancer": 'not active'})
        else:
            return Response(status=status.HTTP_404_NOT_FOUND)