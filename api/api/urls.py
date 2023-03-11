
from django.contrib import admin
<<<<<<< HEAD

from django.urls import path, include

=======
from django.urls import path,include
<<<<<<< HEAD
>>>>>>> 670acac9a8c3f3acaf3fa1a75ededd29389c0c95
from authentication.views import resetPasswordView, emailResetPassword
=======


>>>>>>> mahmoud_abuelhasaan



urlpatterns = [
    path('admin/', admin.site.urls),
    path('auth/',include('authentication.urls')),

<<<<<<< HEAD
    path('reset_password/<uidb64>/<token>/', resetPasswordView, name='reset_password'),
    path('email_reset_password/', emailResetPassword, name='email_reset_password'),
=======
>>>>>>> mahmoud_abuelhasaan


]
