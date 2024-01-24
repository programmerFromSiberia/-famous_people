from django.urls import path, re_path
from django.utils import archive
from .views import *
from django.views.decorators.cache import cache_page

# Эти пути прописать в файле base.html начиная с 20 строчки кода (block mainmenu)

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000/women/
    path('about/',about, name='about'), # прописываем маршут к страницам (шаблонам)
                                        # после этого в файле vievs.py прописываем функции (представления)
    path('addpage/', AddPage.as_view(), name='add_page'), # добавить статью
    path('contact/',ContactFormView.as_view(), name='contact'),  # Обратная связь
    path('login/',LoginUser.as_view(), name='login'),  # прописываем маршут к логину, связываем с классом LoginUser во vievs
    path('logout/',logout_user, name='logout'), # прописываем маршут при нажатии на кнопку выход
                                                # Создадим для Logout_user функцию представления во views
    path('register/', RegisterUser.as_view(), name='register'),  # прописываем маршут к регистрации и vievs создаем этот класс
    path('post/<slug:post_slug>/', ShowPost.as_view(), name='post'),
    path('category/<slug:cat_slug>/', WomenCategory.as_view(), name='category'),
]