from django.contrib import admin
from .models import *


# Регистрация и настройка модели Author
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (при отображении модели)
    list_display = ['__str__', 'last_name', 'first_name', 'date_of_birth', 'date_of_death']


# Регистрация и настройка модели Book
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (при отображении модели)
    list_display = ['__str__', 'genre', 'language', 'get_authors']
    # добавление окошка ФИЛЬТР (по перечисленным полям)
    list_filter = ["genre", "author"]
    # настройка для порядка вывода ПОЛЕЙ, при заполнении экземпляра
    fieldsets = (("Основное", {"fields": ("title", "author")}),
                 ("Дополнительное", {"fields": ("genre", "language", "summary", "isbn")}))

    # Обьявление ВНУТРЕННЕЙ модели "BookInstance" (дополнительная к основной)
    class BookInstanceInline(admin.TabularInline):
        model = BookInstance

    # Дополняем ОСНОВНУЮ "Book" модель дополнительной "BookInstanceInline"
    # (Теперь в редактировании КНИГИ, внизу видны все ее экземпляры)
    inlines = [BookInstanceInline]


# Регистрация и настройка модели BookInstance
@admin.register(BookInstance)
class BookInstanceAdmin(admin.ModelAdmin):
    # Порядок вывода СТОЛБИКОВ (при отображении модели)
    list_display = ["__str__", 'borrower', 'due_back']
    # добавление окошка ФИЛЬТР (по перечисленным полям)
    list_filter = ["status"]
    # настройка для порядка вывода ПОЛЕЙ, при заполнении экземпляра
    fieldsets = (("Экземпляр книги", {"fields": ("book", "imprint", "inv_nom")}),
                 ("Статус окончания и заказы", {"fields": ("borrower", "status", "due_back")}))


# Регистрация и настройка модели Status
@admin.register(Status)
class StatusAdmin(admin.ModelAdmin):
    pass


# Регистрация и настройка модели Language
@admin.register(Language)
class LanguageAdmin(admin.ModelAdmin):
    pass


# Регистрация и настройка модели Genre
@admin.register(Genre)
class GenreAdmin(admin.ModelAdmin):

    # Обьявление ВНУТРЕННЕЙ модели "Book" (дополнительная к основной)
    class BookInline(admin.TabularInline):
        model = Book

    # Дополняем ОСНОВНУЮ "Book" модель дополнительной "BookInstanceInline"
    # (Теперь в редактировании КНИГИ, внизу видны все ее экземпляры)
    inlines = [BookInline]
