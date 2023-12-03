from asgiref.sync import async_to_sync
from rest_framework import generics
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView
import time


from .models import Item
from .serializers import ItemSerializer
from .utils import download_large_file


class ItemListCreateView(generics.ListCreateAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class ItemRetrieveUpdateDestroyView(generics.RetrieveUpdateDestroyAPIView):
    permission_classes = (IsAuthenticated,)
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class DownloadPythonDocs(APIView):
    @async_to_sync
    async def get(self, request):
        start_time = time.time()
        result = await download_large_file('https://docs.python.org/3/archives/python-3.12.0-docs-pdf-letter.zip')
        total = time.time() - start_time
        return Response(f"{result} за {total} секунд")
