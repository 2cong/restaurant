import json

from django.views import View
from django.http import HttpResponse, JsonResponse
from django.db import transaction

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

# 음식점 Create API
class CreateStoreView(View):
    @transaction.atomic
    def post(self, request):
        try:
            restaurant_data = json.loads(request.body)

            # request body를 통해 받은 값을 db에 추가
            Store.objects.create(
                name = restaurant_data['name'],
                description = restaurant_data['description'],
                address = restaurant_data['address'],
                phone_number = restaurant_data['phone_number']
            )

            # db에 추가한 값 중 마지막 id의 정보 불러오기
            new_store = Store.objects.latest('id')

            # 추가된 음식점 정보 불러오기
            restaurant_detail = {
                "id" : new_store.id,
                "name" : new_store.name,
                "description" : new_store.description,
                "address" : new_store.address,
                "phone_number" : new_store.phone_number,
            }

            return JsonResponse({"data":restaurant_detail}, status = 201)

        except KeyError:
            return JsonResponse({"message":"DATA ERROR"}, status = 400)
        except Exception as e:
            return JsonResponse({"message":f"{e}"}, status = 500)
