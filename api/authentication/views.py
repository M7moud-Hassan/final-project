from django.utils.encoding import force_str
from .token import email_verification_token
from rest_framework.decorators import api_view


@api_view(['GET'])
def verfy_email(request,token,uid):
    uid = force_str(uid)
    user = RegisterFreelancer.objects.filter(id=uid)
    if user is not None and email_verification_token.check_token(user, token):
        user.is_activate=True
        return Response(user)
    else:
        return Response(status=status.HTTP_404_NOT_FOUND)
