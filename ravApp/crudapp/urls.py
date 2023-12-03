from django.urls import path

from .views import ItemListCreateView, ItemRetrieveUpdateDestroyView, DownloadPythonDocs

urlpatterns = [
    path('items/', ItemListCreateView.as_view(), name='item-list-create'),
    path('items/<int:pk>/', ItemRetrieveUpdateDestroyView.as_view(), name='item-detail'),
    path('async_download/', DownloadPythonDocs.as_view(), name='vacancies'),
]