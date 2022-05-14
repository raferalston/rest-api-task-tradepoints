from django.core.exceptions import ObjectDoesNotExist

from rest_framework import generics
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import Worker
from .serializers import WorkerSerializer


class WorkerView(generics.ListCreateAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer


class WorkerSearchView(generics.ListAPIView):
    queryset = Worker.objects.all()
    serializer_class = WorkerSerializer

    def get_queryset(self):
        queryset = Worker.objects.all()
        name = self.kwargs.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
            if queryset: return queryset
        raise NotFound(detail=f"Error 404, worker with this name - {name} not found", code=404)