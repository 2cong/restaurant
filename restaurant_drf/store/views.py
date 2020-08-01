from django.http import HttpResponse, JsonResponse

from rest_framework.response import Response
from rest_framework.generics import ListCreateAPIView
from rest_framework.pagination import PageNumberPagination

from .models import Store, Menu
from .serializers import StoreSerializer, MenuSerializer


class StoreListView(ListCreateAPIView):
    def get(self, request):
        restaurants = Store.objects.all()
        serializer = StoreSerializer(restaurants, many=True)

        return Response(serializer.data)
