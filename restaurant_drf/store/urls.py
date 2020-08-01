from django.urls import path
from .views import StoreListView

urlpatterns = [
    path('/list', StoreListView.as_view())
    #path('/detail', DetailView.as_view()),
    #path('', CreateStoreView.as_view()),
    #path('/menu', CreateMenuView.as_view())
    ]
