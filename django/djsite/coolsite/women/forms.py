from django import forms
from django.core.exceptions import ValidationError

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



