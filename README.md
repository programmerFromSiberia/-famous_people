# -famous_people
известные люди

ДЗ 44, ДЗ 45 создал ветку от master ветки назвал ее Test2, в данной ветке я работаю над своим проектом и после проверки кода при отсутствии багов осуществляю слияние (merge) с master  веткой. 

ДЗ 53 Подключил внешние (статические) файлы к шаблонам. Параметры: STATIC_URL, STATIC_ROOT, STATICFILES_DIRS. Загрузка тега static с помощью тега load. Использование тега static в шаблонах. Фильтры шаблонов: linebreaks и truncatewords. Тег autoescape.

ДЗ 54 Сформировал динамические и статические маршруты в шаблонах с помощью тега url и метода модели get_absolute_url(). 

ДЗ 55 (за 05.12.2023 и 06.12.2023)Создал связи между таблицами (моделями) базы данных с помощью класса ForeignKey. Помимо этого рассмотрены Django классы: ManyToManyField и OneToOneField для определения связей многие ко многим и один к одному. Опция on_delete с возможными значениями: CASCADE, PROTECT, SET_NULL, SET_DEFAULT, SET и DO_NOTHING.

ДЗ 57, ДЗ 58, ДЗ 60 Сделал админ-панель на создаваемом сайте. Отдельно рассммотрел: русификацию Django, созданл суперпользователя (createsuperuser), регистрация моделей для админ-панели (функция admin.site.register), провел настройку отображения полей с помощью вложенного класса Meta в классах моделей. Атрибуты: verbose_name, verbose_name_plural, ordering. Также создал вспомогательные классы на основе базового ModelAdmin для дополнительной настройки отображения моделей. Атрибуты: list_display, list_display_links, search_fields, list_editable, list_filter. 
Дополнительно сделано усовершенствование шаблона для отображения изображений в списке статей. 

ДЗ 58 (от 8.01.2024) создал собственные (пользовательские) теги для шаблонов двух типов: simple tags и inclusion tags. Регистрация шаблонных тегов с помощью экземпляра класса Library(). Использование декораторов: simple_tag() и inclusion_tag(). Загрузка и использование пользовательских тегов в шаблонах. Передача параметров пользовательским тегам. 

ДЗ 58 (от 09.01.2024) Определен слаг (slug), в классах моделей через SlugField. Функция get_object_or_404() для получения записи из таблицы. Автоматическое формирование слага в админ-панели (атрибут prepopulated_fields).
12. Создаем форму, не связанной с моделью на основе базового класса Form. с набором полей (CharField, SlugField, BooleanField, ModelChoiceField), обрабатываем данные формы на стороне сервера (метод is_valid() и коллекции cleaned_data и request.POST). Реализовываем способ отображения формы в шаблоне с помощью метода as_p (а также тег csrf_token), определяем стили оформления для полей формы.


