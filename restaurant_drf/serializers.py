from rest_framework import serializers
from snippets.models import Store, Menu

class StoreSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'description', 'address', 'phone_number']

class MenuSerializer(serializers.ModelSerializer):
    store_id = serializers.RelatedField(source='store', read_only = True)

    class Meta:
        model = Menu
        fields = ['id', 'name', 'price', ' store_id']
