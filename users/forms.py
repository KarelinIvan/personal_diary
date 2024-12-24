from users.models import User
from django.contrib.auth.forms import UserCreationForm


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации нового пользователя """
    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')
