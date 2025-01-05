from users.apps import UsersConfig
from django.urls import path
from django.contrib.auth.views import LoginView

from users.views import RegisterView, UserInValidEmail, UserPasswordResetView, email_verification, logout_view, \
    ProfileView

app_name = UsersConfig.name

urlpatterns = [
    path('', LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', logout_view, name='logout'),
    path('registration/', RegisterView.as_view(), name='registration'),
    path("invalid-email/", UserInValidEmail.as_view(), name="invalid_email"),
    path('email-confirm/<str:token>/', email_verification, name='email-confirm'),
    path('reset-password/', UserPasswordResetView.as_view(), name='reset_password'),
    path('profile/', ProfileView.as_view(), name='profile'),
    ]
