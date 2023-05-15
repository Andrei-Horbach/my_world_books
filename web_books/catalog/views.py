from django.shortcuts import render
from django.http import HttpResponse
from .models import *  # Импорт всех моделей
from .forms import *
from django.views import generic  # Нужен для автоматического чтения
from django.contrib.auth.views import LoginView
from django.db.utils import IntegrityError


# Create your views here.


# Главная страница
def index(request):
    # Получаем необходимые данные
    num_books = len(Book.objects.all())  # Количество книг
    num_instances = len(BookInstance.objects.all())  # Количество экземпляров
    num_instances_available = len(BookInstance.objects.filter(status__name="на складе"))
    num_authors = len(Author.objects.all())  # Количество авторов

    # Пример работы с сессиями (подсчитывает кол-во посещений этой страницы)
    # Количество визитов (Получить значение сессии, если не существует - то "0")
    num_visits = request.session.get("num_visits", 0)
    request.session['num_visits'] = int(num_visits) + 1  # Запись нового значения (кол-ва визитов) в сессию

    # Передаем в шаблон
    context = {"num_books": num_books,
               "num_instances": num_instances,
               "num_instances_available": num_instances_available,
               "num_authors": num_authors,
               "num_visits": num_visits}

    return render(request, 'index.html', context=context)


# Страница регистрации аккаунта
def registration(request):
    if request.method == "GET":
        # Создание формы:
        form = Registration()
        # Генерация данных (context)
        context = {"form": form}
        # Показываем шаблон
        return render(request, "registration/registration.html", context=context)

    if request.method == "POST":
        # Получаем данные из формы
        username = request.POST.get("username")
        password = request.POST.get("password")
        email = request.POST.get("email", "")
        try:
            # Записываем данные в БД (нового пользователя)
            User.objects.create_user(username, password, email).save()
            # Генерация данных (context)
            context = {"username": username}
            # Показываем шаблон
            return render(request, "registration/registration.html", context=context)
        except IntegrityError:
            # Генерация данных (context)
            context = {"error": username}
            # Показываем шаблон
            return render(request, "registration/registration.html", context=context)


# Страница входа в аккаунт (Переназначение)
class LoginUser(LoginView):
    form_class = Login
    template_name = "registration/login.html"


# Возвращает список всех книг. (Автоматически генерируется при помощи ListView)
# Шаблон "templates/catalog/book_list.html"
# Переменная (шаблона/ключ): "book_list"
class BookListView(generic.ListView):
    model = Book
    paginate_by = 2  # Сколько обьектов будет передано в шаблон


# Возвращает конкретную книгу. (Автоматически генерируется при помощи DetailView)
# Шаблон "templates/catalog/book_detail.html"
# Переменная (входная): "int:pk"
# Переменная (шаблона/ключ): "book"
class BookDetailView(generic.DetailView):
    model = Book


# Возвращает всех Авторов. (Автоматически генерируется при помощи ListlView)
# Шаблон "templates/catalog/author_list.html"
# Переменная (входная): ""
# Переменная (шаблона/ключ): "author_list"
class AuthorListView(generic.ListView):
    model = Author
    paginate_by = 3  # Сколько обьектов будет передано в шаблон
