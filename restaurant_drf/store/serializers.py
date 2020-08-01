from rest_framework import serializers

class StoreSerializer(serializers.Serializer):
    id = serializers.IntegerField(read_only=True)
    name = serializers.CharField(max_length=50)
    description = serializers.CharField(max_length=2000)
    address = serializers.CharField(max_length=100)
    phone_number = serializers.CharField(max_length=20)
