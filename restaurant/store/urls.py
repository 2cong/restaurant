from django.urls import path
from .views import DetailView, CreateStoreView, CreateMenuView

urlpatterns = [
    path('/detail', DetailView.as_view()),
    path('', CreateStoreView.as_view()),
    path('/menu', CreateMenuView.as_view())
    ]
