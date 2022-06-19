from django.contrib import admin

from .models import Author, Todo, Project

admin.site.register(Author)
admin.site.register(Todo)
admin.site.register(Project)
