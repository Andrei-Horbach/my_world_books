from django.db import models
from django.contrib.auth.models import User  # импортируем встроенную модель "Пользователи"


# 1. Модель Жанры (Genre)
# Поля: name(жанр)
class Genre(models.Model):
    name = models.CharField(max_length=200,
                            help_text="Введите жанр книги",
                            verbose_name="Жанр Книги")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Жанр"  # Название модели в ед. Числе
        verbose_name_plural = "Жанры"  # Название модели во мн. Числе
        ordering = ["name"]  # Сортировка по полю


# 2. Модель Авторы (Author)
# Поля: first_name(Имя автора), last_name(Фамилия), date_of_birth(дата рождения), date_of_death(дата смерти)
class Author(models.Model):
    first_name = models.CharField(max_length=100, help_text="Введите имя автора", verbose_name="Имя автора")
    last_name = models.CharField(max_length=100, help_text="Введите фамилию автора", verbose_name="Фамилия автора")
    date_of_birth = models.DateField(null=True, blank=True, help_text="Введите дату рождения",
                                     verbose_name="дата рождения")
    date_of_death = models.DateField(null=True, blank=True, help_text="Введите дату смерти", verbose_name="дата смерти")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return "{} {}".format(self.first_name, self.last_name)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Автора"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Авторы"  # Название модели во мн. числе
        ordering = ["last_name"]  # Сортировка по полю (если со знаком "-" то в обратном порядке)


# 3. Модель Язык (Language)
# Поля: name(Язык)
class Language(models.Model):
    name = models.CharField(max_length=20, help_text="Введите язык книги", verbose_name="Язык книги")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Язык"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Языки"  # Название модели во мн. числе
        ordering = ["name"]  # Сортировка по полю


# 4. Модель Книг (Books)
# Поля (со связями): author(Автор-ManyToManyField), genre(Жанр-ForeignKey), language(Язык-ForeignKey),
# Поля (обычные): title(Название), summary(Описание), isbn(Код книги)
class Book(models.Model):
    objects = None
    author = models.ManyToManyField(Author, help_text="Выберите автора книги", verbose_name="Автор книги")
    genre = models.ForeignKey(Genre, null=True, on_delete=models.CASCADE, help_text="Выберите жанр книги", verbose_name="Жанр книги")
    language = models.ForeignKey(Language, null=True, on_delete=models.CASCADE, help_text="Выберите язык книги", verbose_name="Язык книги")
    title = models.CharField(max_length=200, help_text="Введите название книги", verbose_name="Название книги")
    summary = models.TextField(max_length=1000, help_text="Введите описание книги", verbose_name="Описание книги")
    isbn = models.CharField(max_length=200, help_text="Должно содержать 13 символов", verbose_name="ISBN книги")

    # [ВНУТРЕННИЙ МЕТОД]. Получить все фамилии авторов книг (Метод показа [всех авторов]). НУЖЕН ЕСЛИ СВЯЗЬ ManyToManyField !!
    def get_authors(self):
        # 1 способ
        # lst_authors = [a.last_name for a in self.author.all()]
        # str_authors = str(lst_authors)

        # 2 способ
        lst_authors = []
        for author in self.author.all():
            lst_authors.append(author.last_name)
        return ", ".join(lst_authors)

    # [ВНУТРЕННИЙ МЕТОД]. Метод возвращающий ссылку на книгу
    def get_absolute_url(self):
        return "/book/{}".format(self.pk)  # self.pk тоже самое что self.id

    # Подписать столбик (что бы при выводе названии, колонка была не как название функции, а как укажем)
    get_authors.short_description = "Авторы"

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.title

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Книгу"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Книги"  # Название модели во мн. числе
        ordering = ["title"]  # Сортировка по полю


# 5. Модель Состояние (Status)
# Поля: name(Состояние)
class Status(models.Model):
    name = models.CharField(max_length=20, help_text="Введите статус экземпляра книги",
                            verbose_name="Статус экземпляра книги")

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return self.name

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Статус"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Статусы"  # Название модели во мн. числе
        ordering = ["name"]  # Сортировка по полю


# 6. Модель Экземпляр (BookInstance)
# Поля (связи): book(Книга-OneToManyField), status(Статус-ForeignKey), borrower(Заказчик - ForeignKey)
# Поля (обычные): due_back(Дата возврата), imprint(Издательство), inv_nom(Инвентарный номер)
class BookInstance(models.Model):
    book = models.ForeignKey(Book, on_delete=models.CASCADE, null=True, help_text="Введите название книги", verbose_name="Название книги")
    inv_nom = models.CharField(max_length=20, null=True, help_text="Введите инвентарный номер экземпляра",
                               verbose_name="Инвентарный номер")
    imprint = models.CharField(max_length=200, help_text="Введите издательство и год выпуска",
                               verbose_name="Издательство")
    status = models.ForeignKey(Status, on_delete=models.CASCADE, null=True, help_text='Изменить состояние экземпляра',
                               verbose_name="Статус экземпляра книги")
    due_back = models.DateField(null=True, blank=True, help_text="Введите конец срока статуса",
                                verbose_name="Дата окончания статуса")
    borrower = models.ForeignKey(User, on_delete=models.SET_NULL, null=True, blank=True, help_text="Заказчик", verbose_name="Выберите заказчика книги")

    # [ВНУТРЕННИЙ МЕТОД]. Проверка не просрочен ли срок возврата книги.
    pass

    # При просмотре всей модели из админки (поле которое будет отображаться)
    def __str__(self):
        return '№{}, {}, ({})'.format(self.inv_nom, self.book, self.status)

    # НАСТРОЙКИ перевода модели и сортировки объектов на главной таблице
    class Meta:
        verbose_name = "Экземпляр"  # Название модели в ед. числе род. падежа
        verbose_name_plural = "Экземпляры"  # Название модели во мн. числе
        ordering = ["inv_nom"]  # Сортировка по полю
