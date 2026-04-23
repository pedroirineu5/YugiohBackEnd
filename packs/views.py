from rest_framework import generics

from packs.models import Pack
from packs.serializers import PackSerializer


class PacksCreateListView(generics.ListCreateAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer


class PacksRetrieveUpdateDestroy(generics.RetrieveUpdateDestroyAPIView):
    queryset = Pack.objects.all()
    serializer_class = PackSerializer
