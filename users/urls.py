from users.apps import UsersConfig
from django.urls import path

from users.views import RegisterView

app_name = UsersConfig.name

urlpatterns = [
    path('registration/', RegisterView.as_view(), name='registration'),

    ]
