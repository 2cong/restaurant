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

            # 레스토랑 정보 및 해당 정보 받아오기
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
        except Exception as e:
            return JsonResponse({"message":f"{e}"}, status = 500)

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

# 메뉴 Create API
class CreateMenuView(View):
    @transaction.atomic
    def post(self, request):
        try:
            menu_data = json.loads(request.body)

            # 해당 음식점에 menu 추가하기 위해서 restaurant_id 받아옴
            restaurant_id = request.GET['restaurant_id']

            # 해당 음식점이 존재하지 않으면 에러처리
            if Store.objects.filter(id=restaurant_id).exists() is False:
                return JsonResponse({"message":"DATA ERROR"}, status = 400)

            # request body를 통해 받은 값을 db에 추가
            Menu.objects.create(
                store_id = Store.objects.get(id=restaurant_id),
                name = menu_data['name'],
                price = menu_data['price']
            )

            # db에 추가한 값 중 마지막 id의 정보 불러오기
            new_menu = Menu.objects.latest('id')

            # 추가된 메뉴 정보 불러오기
            menu = {
                "id": new_menu.id,
                "name": new_menu.name,
                "price": new_menu.price
            }

            return JsonResponse({"data":menu}, status = 201)

        except KeyError:
            return JsonResponse({"message":"DATA ERROR"}, status = 400)
        except Exception as e:
            return JsonResponse({"message":f"{e}"}, status = 500)
