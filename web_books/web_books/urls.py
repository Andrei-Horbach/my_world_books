from django.contrib import admin
from django.urls import path, include
from catalog import views

urlpatterns = [
    # Админка и Аккаунты

    path('admin/', admin.site.urls),
    path('accounts/login/', views.LoginUser.as_view(), name="login"),  # Маршрут для входа (Переназначение)
    path('accounts/', include("django.contrib.auth.urls")),  # Маршрут для работы с аккаунтами
    path('accounts/registration', views.registration, name="registration"),  # Маршрут для регистрации

    # Статические маршруты
    path('', views.index, name="index"),  # Главная страница
    path('books/', views.BookListView.as_view(), name="books"),  # Все книги (/books/?page=2)
    path('authors/', views.AuthorListView.as_view(), name="authors"),  # Все авторы
    # Страница. Список всех экземпляров прикрепленных к пользователю

    # Динамические маршруты (название переменной обязательно: "pk")
    path('book/<int:pk>', views.BookDetailView.as_view(), name="book"),  # Конкретная книга

    # Страницы касательно [Редактирования авторов] 4шт.
    # Страницы касательно [Редактирования книг] 3шт.

]
