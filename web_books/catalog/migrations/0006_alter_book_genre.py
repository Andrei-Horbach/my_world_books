# Generated by Django 4.1.7 on 2023-04-04 18:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0005_alter_book_options_alter_genre_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='genre',
            field=models.ForeignKey(help_text=' Выберите жанр для книги', on_delete=django.db.models.deletion.CASCADE, to='catalog.genre', verbose_name='Жанр книги'),
        ),
    ]
