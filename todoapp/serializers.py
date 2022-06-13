from rest_framework.serializers import HyperlinkedModelSerializer
from .models import Todo, Project, Author
from rest_framework.serializers import ModelSerializer


class TodoModelSerializer(ModelSerializer):
    class Meta:
        model = Todo
        fields = "__all__"


class AuthorModelSerializerHyper(HyperlinkedModelSerializer):
    class Meta:
        model = Author
        fields = "__all__"


class AuthorModelSerializer(ModelSerializer):
    class Meta:
        model = Author
        fields = "__all__" 


class ProjectModelSerializer(ModelSerializer):
    class Meta:
        model = Project
        fields = "__all__" 


class ProjectModelSerializerHyper(HyperlinkedModelSerializer):
    class Meta:
        model = Project
        fields = "__all__"       


