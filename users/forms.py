from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, PasswordResetForm
from django.forms import BooleanField

from users.models import User


class StyleFormMixin:
    """ используется для настройки атрибутов виджетов форм в Django """

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        for field_name, field, in self.fields.items():
            if isinstance(field, BooleanField):
                field.widget.attrs['class'] = 'form-check-input'
            else:
                field.widget.attrs['class'] = 'form-control'


class UserRegisterForm(UserCreationForm):
    """ Форма для регистрации нового пользователя """
    email = forms.EmailField(required=True, label="Email",
                             widget=forms.EmailInput(attrs={'placeholder': 'Введите e-mail'}))
    password1 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Введите пароль'}), label="Пароль")
    password2 = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder': 'Повторите пароль'}),
                                label="Повторите пароль")

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


class ResetPasswordForm(StyleFormMixin, PasswordResetForm):
    """ Форма для сброса пароля """

    class Meta:
        model = User
        fields = ('email',)
