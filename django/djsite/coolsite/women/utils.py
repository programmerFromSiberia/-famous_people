from django.db.models import Count

from .models import *

menu = [{'title': "О сайте", 'url_name': 'about'},
        {'title': "Добавить статью", 'url_name': 'add_page'},
        {'title': "Обратная связь", 'url_name': 'contact'},
]

class DataMixin:
    paginate_by = 20  # количество элементов на одной странице = 3

    def get_user_context(self, **kwargs):
        context = kwargs
        cats = Category.objects.annotate(Count('women'))  # если у нас есть рубрика но в ней нет постов то она не отображается

        user_menu = menu.copy()  # если пользователь не авторизован то в меню убираем "Добавить статью"
        if not self.request.user.is_authenticated:  #  используем аутентификацию is_authenticated
            user_menu.pop(1)

        context['menu'] = user_menu

        context['cats'] = cats  # если пользователь авторизован то увидит все строчки меню
        if 'cat_selected' not in context:
            context['cat_selected'] = 0
        return context