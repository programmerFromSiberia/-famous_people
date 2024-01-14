from django.db import models
from django.urls import reverse

# описание полей таблицы берем из справочника Django
# https://docs.djangoproject.com/en/5.0/ref/models/fields/

class Women(models.Model): # создаем таблицу базы данных со столбцами
    title = models.CharField(max_length=255, verbose_name= 'Заголовок')  # заголовок статьи
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name= 'URL')
    content = models.TextField(blank=True, verbose_name= 'Текст статьи')  # контент
    photo = models.ImageField(upload_to=True, verbose_name= 'Фото')  # фото лежит в подкаталоге  upload_to
    time_create = models.DateTimeField(auto_now_add=True, verbose_name= 'Время создания')  # время создания статьи
    time_update = models.DateTimeField(auto_now=True, verbose_name= 'Время изменения')  # время его изменения
    is_published = models.BooleanField(default=True, verbose_name= 'Публикация')  # опубликована статья или нет
    cat = models.ForeignKey('Category', on_delete=models.PROTECT, verbose_name= 'Категория')

    def __str__(self):
        return self.title

    # формируем динамическую ссылку на  url-адрес в папке urls.py

    def get_absolute_url(self):
        return reverse('post', kwargs={'post_slug': self.slug})

    # далее  переходим в папку index.html и в строчке кода 11 прописываем команду
    # {% p.get_absolute_url %}

    # настраиваем мета-сласс (подкласс)
    class Meta:
        verbose_name = 'Известные женщины'
        verbose_name_plural = 'Известные женщины' # убираем букву "s" в админ панели
        # добавляем сортировку по полям (указываем какие поля) в админ панели
        ordering = ['id']
#(урок 5)

# Создаем файл миграции пописав в консоли команду "python manage.py makemigrations"

# в терминале пишем команду E:\python\django\djsite\coolsite> python manage.py shell и заходим в консоль
# импортируем модель командой from women.models import Women
# заполняем поля таблицы данными, командой Women(title='Анжелина Джоли', content='Биография Анжелины Джоли')
# создаем переменную для дальнейшего сохранения записи командой w1 = _
# сохраняем созданную запись в таблице w1.save()
# импортируем модуль connection командой from django.db import connection
# заполняем следующее поле таблицы с помощью новой переменной w2 командой w2 = Women(title='Энн Хэтэуэй', content='Биография Энн Хэтэуэй')
# w2.save() сохраняем
# w2 = _  записываем
# -------- можно заполнять по другому-------
# w3 = Women()
# w3.title = 'Джулия Робертс'
# w3.content = 'Биография Джулии Робертс'
# w3.save()
#-------------------------------------------
# ---САМЫЙ ПРОСТОЙ МЕТОД ДОБАВЛЕНИЯ ЗАПИСЕЙ В ТАБЛИЦУ--- через objects и его метод .create
# w4 = Women.objects.create(title='Ума Турман', content='Биография Умы Турман')
#
# ----------------изменение записи в поле content-------------
# wu = Women.objects.get(pk=5) вызываем строку 5
# wu.content = 'Биография Киры Найтли' переприсваеваем значение
# wu.save() записываем изменения



#Устанавливаем связь между таблицей базы данных и категориями страниц сайта

class Category(models.Model):
    name = models.CharField(max_length=100, db_index=True, verbose_name='Категория')
    slug = models.SlugField(max_length=255, unique=True, db_index=True, verbose_name='URL')
    def __str__(self):
        return self.name

    def get_absolute_url(self):  # добавляем кнопку (смотреть на сайте) в админ панели http://127.0.0.1:8000/admin/
        return reverse('category', kwargs={'cat_slug':self.slug})

    class Meta:
        verbose_name = 'Категорию'
        verbose_name_plural = 'Категории' # убираем букву "s" в админ панели
        ordering = ['id']




