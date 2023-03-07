from django.contrib.auth import get_user_model
from django.utils.encoding import force_str
from .token import email_verification_token

from rest_framework.decorators import api_view


@api_view(['GET'])
def verfy_email(request,token,uid):
    print(token)
    print(uid)
    try:
        uid = force_str(uid)
        # user = RegisterFreelancer.objects.filter(id=uid)
        user = get_user_model().objects.get(id=uid)
    except (TypeError, ValueError, OverflowError, get_user_model().DoesNotExist):
        return None

    if user is not None and email_verification_token.check_token(user, token):
        return "OK"

    return None
