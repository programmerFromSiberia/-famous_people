from django.urls import path, re_path
from django.utils import archive

from .views import *

# Эти пути прописать в файле base.html начиная с 20 строчки кода (block mainmenu)

urlpatterns = [
    path('', WomenHome.as_view(), name='home'),  # http://127.0.0.1:8000/women/
    path('about/',about, name='about'), # прописываем маршут к страницам (шаблонам)
                                        # после этого в файле vievs.py прописываем функции (представления)
    path('addpage/', addpage, name='add_page'),
    path('contact/',contact, name='contact'),
    path('login/',login, name='login'),
    path('post/<slug:post_slug>/', show_post, name='post'),
    path('category/<int:cat_id>/', show_category, name='category'),
]