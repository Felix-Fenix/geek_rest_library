from django.db import models
from pkg_resources import to_filename

class Author(models.Model):
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    birthday_year = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    
    def __str__(self):
        return self.last_name

class Todo(models.Model):
    new_project = models.CharField(verbose_name="Название проекта",max_length=32)
    note = models.CharField(verbose_name="Заметка", max_length=5000)
    create_todo = models.DateTimeField(verbose_name="Время создания")
    update_todo = models.DateTimeField(verbose_name="Время последнего обновления", auto_now_add=True)
    author = models.ForeignKey(verbose_name="Автор заметки", max_length=64, to=Author, on_delete=models.CASCADE)
    activ_is = models.BooleanField(verbose_name="Активность заметки")

    def __str__(self):
        return self.author


class Project(models.Model):
    name = models.CharField(verbose_name="Название проекта", max_length=128)
    link = models.URLField(verbose_name="Ссылка на проект") 
    authors = models.ManyToManyField(verbose_name="Авторы заметок",to=Author)

