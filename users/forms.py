from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm

from users.models import User


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации нового пользователя """

    # email = forms.EmailField(required=True, widget=forms.EmailInput(attrs={'placeholder': 'Введите e-mail'}))
    # password1 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}))
    # password2 = forms.CharField(required=True, widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль повторно'}))

    class Meta:
        model = User
        fields = ('email', 'password1', 'password2')


class UserProfileForm(UserChangeForm):
    """ Профиль пользователя """

    class Meta:
        model = User
        fields = ('email', 'phone', 'city', 'avatar')

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields['password'].widget = forms.HiddenInput()


class ResetPasswordForm(PasswordResetForm):
    """ Форма для сброса пароля """

    class Meta:
        model = User
        fields = ('email',)
