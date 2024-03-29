from django import forms
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from captcha.fields import CaptchaField


from .models import *

class AddPostForm(forms.ModelForm): # создаем таблицу базы данных со столбцами
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['cat'].empty_label = "Категория не выбрана"
    class Meta:
        model = Women  # связываем с Women
        fields = ['title', 'slug', 'content', 'photo', 'is_published', 'cat']  # указываем те поля что будут отображаюстя в форме
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-input'}),
            'content': forms.Textarea(attrs={'cols': 60, 'rows': 10}),
        }
# Создаем валидатор (проверка) заголовка title на длинну символов
    def clean_title(self):
        title = self.cleaned_data['title']
        if len(title) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return title

    def clean_content(self):
        content = self.cleaned_data['content']
        if len(content) > 200:
            raise ValidationError('Длина превышает 200 символов')

        return content

# улучшаем вид формы регистрации пользователя, добавляем поля с помощью виджетов оформляем вышеуказанные поля

class RegisterUserForm(UserCreationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    email = forms.EmailField(label='Email', widget=forms.EmailInput(attrs={'class': 'form-input'}))
    password1 = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))
    password2 = forms.CharField(label='Повтор пароля', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

    class Meta:
        model = User  # работает с таблицей базы данных
        fields = ('username', 'email', 'password1', 'password2')  # отображение полей таблицы


# улучшаем форму авторизации с помощью виджетов с помощью виджетов оформляем вышеуказанные поля
# username, password, класс Мета можно не применять.
class LoginUserForm(AuthenticationForm):
    username = forms.CharField(label='Логин', widget=forms.TextInput(attrs={'class': 'form-input'}))
    password = forms.CharField(label='Пароль', widget=forms.PasswordInput(attrs={'class': 'form-input'}))

class ContactForm(forms.Form):
    name = forms.CharField(label='Имя', max_length=255)
    email = forms.EmailField(label='Email')
    content = forms.CharField(widget=forms.Textarea(attrs={'cols': 60, 'rows': 10}))
    captcha = CaptchaField()



