from django.shortcuts import render
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from .models import ProductItems
from .serializers import ProductItemsSerializer
from rest_framework.authentication import TokenAuthentication
from rest_framework.permissions import IsAuthenticated


# Create your views here.

class ProductItemsListCreateView(ListCreateAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProductItems.objects.using("mongo").all()
    serializer_class = ProductItemsSerializer

    def perform_create(self, serializer):
        instance = serializer.custom_create_method(serializer.validated_data)
        return instance


class ProductItemsRetrieveUpdateDestroyView(RetrieveUpdateDestroyAPIView):
    authentication_classes = [TokenAuthentication]
    permission_classes = [IsAuthenticated]
    queryset = ProductItems.objects.using("mongo").all()
    serializer_class = ProductItemsSerializer

    def perform_update(self, serializer):
        instance = serializer.update_custom(serializer.instance, serializer.validated_data)
        return instance

    def perform_destroy(self, instance):
        serializer = self.get_serializer(instance)
        serializer.delete_custom(instance)

