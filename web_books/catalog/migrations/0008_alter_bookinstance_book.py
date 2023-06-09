# Generated by Django 4.1.7 on 2023-04-04 18:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0007_bookinstance_borrower'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bookinstance',
            name='book',
            field=models.ForeignKey(help_text='Введите название книги', null=True, on_delete=django.db.models.deletion.CASCADE, to='catalog.book', verbose_name='Название книги'),
        ),
    ]
