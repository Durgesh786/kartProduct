from .views import ProductItemsListCreateView,ProductItemsRetrieveUpdateDestroyView
from django.urls import path

app_name = "product"
urlpatterns = [
    path('item/', ProductItemsListCreateView.as_view(), name='product-list-create'),
    path('item/<int:pk>/', ProductItemsRetrieveUpdateDestroyView.as_view(), name='product-retrieve-update-destroy'),
]