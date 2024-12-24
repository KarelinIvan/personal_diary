from users.apps import UsersConfig
from django.urls import path

from users.views import UserRegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', UserRegisterView.as_view(template_name='users/registration.html'), name='registration'),

    ]
