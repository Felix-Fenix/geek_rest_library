from pkg_resources import to_filename
from rest_framework.viewsets import ModelViewSet
from .models import Todo, Project, Author
from .serializers import (ProjectModelSerializer, TodoModelSerializer, ProjectModelSerializerHyper,
 AuthorModelSerializer, AuthorModelSerializerHyper, ProjectModelSerializer)
from rest_framework.decorators import api_view, renderer_classes
from rest_framework.renderers import JSONRenderer, BrowsableAPIRenderer
from rest_framework import viewsets
from rest_framework.generics import RetrieveAPIView, UpdateAPIView, ListAPIView
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.decorators import action
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
 


class AuthorRetrieveAPIView(RetrieveAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializerHyper


class AuthorUpdateAPIView(UpdateAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializerHyper    


class AuthorListAPIView(ListAPIView):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializerHyper


class AuthorModelViewSet(ModelViewSet):
    queryset = Author.objects.all()
    serializer_class = AuthorModelSerializer


###############################


class TodoLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2


class TodoModelViewSet(ModelViewSet):
    queryset = Todo.objects.all()
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination


class Todo_DELETE_ViewSet(viewsets.ViewSet):
    renderer_classes = [JSONRenderer, BrowsableAPIRenderer]

    @action(detail=True, methods=['delete'])
    def todo_is_activ_False(self, request, pk=None):
        new_activ = get_object_or_404(Todo, pk=pk)
        new_activ.activ_is = False
        new_activ.save()
        serializer = TodoModelSerializer(new_activ)
        return Response({'Состояние заметки': new_activ.activ_is})


    def list(self, request):
        todo = Todo.objects.all()
        serializer = TodoModelSerializer(todo, many=True)
        return Response(serializer.data)

      
    def retrieve(self, request, pk=None):
        todo = get_object_or_404(Todo, pk=pk)
        serializer = TodoModelSerializer(todo)
        return Response(serializer.data)


class TodoKwargsFilterView(ListAPIView):
    serializer_class = TodoModelSerializer
    pagination_class = TodoLimitOffsetPagination
    def get_queryset(self):
        new_project = self.kwargs['new_project']
        return Todo.objects.filter(new_project__contains=new_project)


####################################


class ProjectLimitOffsetPagination(LimitOffsetPagination):
    default_limit = 2  


class ProjectLimitOffsetPaginatonViewSet(viewsets.ModelViewSet):
    queryset = Project.objects.all()
    serializer_class = ProjectModelSerializerHyper    
    pagination_class = ProjectLimitOffsetPagination


class ProjectKwargsFilterView(ListAPIView):
    serializer_class = ProjectModelSerializer

    def get_queryset(self):
        name = self.kwargs['name']
        return Project.objects.filter(name__contains=name)