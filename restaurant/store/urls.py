from django.urls import path
from .views import ListView, DetailView, CreateStoreView, CreateMenuView

urlpatterns = [
    path('/list', ListView.as_view()),
    path('/detail', DetailView.as_view()),
    path('', CreateStoreView.as_view()),
    path('/menu', CreateMenuView.as_view())
    ]
