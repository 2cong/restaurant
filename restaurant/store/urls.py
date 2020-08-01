from django.urls import path
from .views import DetailView, CreateStoreView

urlpatterns = [
    path('/detail',DetailView.as_view()),
    path('',CreateStoreView.as_view())
    ]
