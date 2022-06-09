from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Todo, Project 


class TodoModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class ProjectModelSerializer(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"       

