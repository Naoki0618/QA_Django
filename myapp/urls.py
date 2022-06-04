from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('<int:pk>/detail/', views.detail, name='detail'),
    path('<int:pk>/answer/', views.answer, name='answer'),
    path('<int:pk>/edit/', views.edit, name='edit'),
    path('<int:pk>/delete/', views.delete, name='delete'),
    path('myapp/find', views.find, name='find'),
]