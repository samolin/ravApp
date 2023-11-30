from django.urls import path

from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('item`s/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),
]