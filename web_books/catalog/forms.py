from django import forms
from django.contrib.auth.forms import AuthenticationForm


# Создание формы Регистрации
class Registration(forms.Form):
    username = forms.CharField(label="Логин", max_length=10, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "username"}))
    password = forms.CharField(label="Пароль", widget=forms.widgets.PasswordInput(
        attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "username"}))
    email = forms.EmailField(label="Email", required=False, help_text="(не обязательно)",
                             widget=forms.widgets.EmailInput(
                                 attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "username"}))


# Переназначение (На основе наследования) формы Входа
class Login(AuthenticationForm):
    username = forms.CharField(label="Логин", max_length=10, widget=forms.widgets.TextInput(
        attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "username"}))
    password = forms.CharField(label="Пароль", widget=forms.widgets.PasswordInput(
        attrs={'class': 'form-control', 'id': "floatingInput", "placeholder": "username"}))
