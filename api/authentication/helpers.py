from django.core.mail import send_mail
import uuid
from django.conf import settings
def send_forget_password_mail(email , token):
    token = str(uuid.uuid4())
    subject = 'the link to change the password'
    message = f'Hi , click on the following link to change your Password http://127.0.0.1/8000/changePassword/{token}/'
    email_from = settings.EMAIL_HOST_USER
    recipient_list = [email]
    send_mail(subject, message, email_from, recipient_list)
    return True