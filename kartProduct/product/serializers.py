from rest_framework import serializers
from .models import *


class ProductItemsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductItems
        fields = '__all__'

    def custom_create_method(self, validated_data):
        instance = ProductItems.objects.using("mongo").create(**validated_data)
        return instance

    def update_custom(self, instance, validated_data):
        instance = ProductItems.objects.using("mongo").get(id=instance.id)
        instance.name = validated_data.get('name', instance.name)
        instance.price = validated_data.get('price', instance.name)
        instance.save()
        return instance

    def delete_custom(self, instance):
        instance = ProductItems.objects.using("mongo").get(id=instance.id)
        instance.delete()
