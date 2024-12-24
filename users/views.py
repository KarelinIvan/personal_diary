from django.views.generic import CreateView

from users.forms import UserRegisterForm
from users.models import User


class UserRegisterView(CreateView):
    """ Регистрация нового пользователя """
    model = User
    form_class = UserRegisterForm
    template_name = 'users/registration.html'
