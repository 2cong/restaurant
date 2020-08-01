import json

from django.views import View
from django.http import HttpResponse, JsonResponse
from .models import Menu, Store

# 음식점 Detail API
class DetailView(View):
    def get(self, request):
        try:
            restaurant_id = request.GET['restaurant_id']

            restaurant_information = Store.objects.get(id=restaurant_id)
            menu_information = Menu.objects.select_related('store_id').filter(store_id=restaurant_id)

            restaurant_detail = {
                "id" : restaurant_information.id,
                "name" : restaurant_information.name,
                "description" : restaurant_information.description,
                "address" : restaurant_information.address,
                "phone_number" : restaurant_information.phone_number,
                "menus": [
                    {
                        "id" : menu.id,
                        "name" : menu.name,
                        "price" : menu.price
                    }for menu in menu_information
                ]
            }

            return JsonResponse({"data":restaurant_detail}, status = 200)

        except KeyError:
            return JsonResponse({"message":"DATA ERROR"}, status = 400)
