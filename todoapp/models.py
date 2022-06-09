from django.db import models



class Todo(models.Model):
    new_project = models.CharField(verbose_name="Название проекта",max_length=32)
    note = models.CharField(verbose_name="Заметка", max_length=5000)
    create_todo = models.PositiveIntegerField(verbose_name="Время создания")
    update_todo = models.PositiveIntegerField(verbose_name="Время последнего обновления")
    author = models.CharField(verbose_name="Автор заметки",max_length=64)
    activ_is = models.BooleanField(verbose_name="Активность заметки")

    def __str__(self):
        return self.author


class Project(models.Model):
    name = models.CharField(verbose_name="Название проекта", max_length=128)
    link = models.URLField(verbose_name="Ссылка на проект") 
    authors = models.ManyToManyField(verbose_name="Авторы заметок",to=Todo)

