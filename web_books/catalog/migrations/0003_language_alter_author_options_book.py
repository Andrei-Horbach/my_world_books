# Generated by Django 4.1.7 on 2023-04-04 17:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0002_author_alter_genre_options'),
    ]

    operations = [
        migrations.CreateModel(
            name='Language',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Введите язык книги', max_length=20, verbose_name='Язык книги')),
            ],
            options={
                'verbose_name': 'Язык',
                'verbose_name_plural': 'Языки',
                'ordering': ['name'],
            },
        ),
        migrations.AlterModelOptions(
            name='author',
            options={'ordering': ['last_name'], 'verbose_name': 'Автора', 'verbose_name_plural': 'Авторы'},
        ),
        migrations.CreateModel(
            name='Book',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(help_text='Введите название книги', max_length=200, verbose_name='Название книги')),
                ('summary', models.TextField(help_text='Введите краткое описание книги', max_length=1000, verbose_name='Аннотация книги')),
                ('isbn', models.CharField(help_text='Должно содержать 13 символов', max_length=13, verbose_name='ISBN книги')),
                ('author', models.ManyToManyField(help_text='Выберите автора книги', null=True, to='catalog.author', verbose_name='Автор книги')),
                ('genre', models.ForeignKey(help_text=' Выберите жанр для книги', on_delete=django.db.models.deletion.CASCADE, to='catalog.genre')),
                ('language', models.ForeignKey(help_text='Выберите язык книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.language', verbose_name='Язык книги')),
            ],
            options={
                'verbose_name': 'Книга',
                'verbose_name_plural': 'Книги',
                'ordering': ['title'],
            },
        ),
    ]
