from re import M
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken import views as vw
from todoapp.views import (TodoModelViewSet, AuthorListAPIView,
 AuthorRetrieveAPIView, AuthorUpdateAPIView, ProjectLimitOffsetPaginatonViewSet,
  AuthorModelViewSet, Todo_DELETE_ViewSet, TodoKwargsFilterView, ProjectKwargsFilterView)
from todoapp import views


router = DefaultRouter()
router.register('author', AuthorModelViewSet)
router.register('false_activ_is', views.Todo_DELETE_ViewSet, basename='todo')
router.register('todo', TodoModelViewSet)
pagination_router = DefaultRouter()
pagination_router.register('limitoffset', views.ProjectLimitOffsetPaginatonViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api-auth/', include('rest_framework.urls')),
    path('api/', include(router.urls)),
    path('generic/List/', views.AuthorListAPIView.as_view()),
    path('generic/retrieve/<int:pk>/', views.AuthorRetrieveAPIView.as_view()),
    path('generic/update/<int:pk>/', views.AuthorUpdateAPIView.as_view()),
    path('pagination/', include(pagination_router.urls)),
    path('filters/kwargs/project/<str:name>/', views.ProjectKwargsFilterView.as_view()),
    path('filters/kwargs/todo/<str:new_project>/', views.TodoKwargsFilterView.as_view()),
    path('api-token-auth/', vw.obtain_auth_token)
]
