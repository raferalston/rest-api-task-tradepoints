from rest_framework import generics, status
from rest_framework.exceptions import NotFound
from rest_framework.response import Response

from .models import TradePoint, Visit
from .permissions import TradePointPermission, VisitPointPermission
from .serializers import TradePointSerializer, VisitSerializer, WorkerTradepointSerializer


class TradePointList(generics.ListCreateAPIView):
    queryset = TradePoint.objects.all()
    serializer_class = TradePointSerializer


class TradePointDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = TradePoint.objects.all()
    serializer_class = TradePointSerializer


class TradePointSearchView(generics.ListAPIView):
    queryset = TradePoint.objects.all()
    serializer_class = TradePointSerializer

    def get_queryset(self):
        queryset = TradePoint.objects.all()
        name = self.kwargs.get('name')
        if name is not None:
            queryset = queryset.filter(name=name)
            if queryset: return queryset
        raise NotFound(detail=f"Error 404, trade point with this name - {name} not found", code=404)


class WorkerTradepointView(generics.ListAPIView):
    queryset = TradePoint.objects.all()
    serializer_class = WorkerTradepointSerializer
    permission_classes = [TradePointPermission]


class WorkerVisitTradePointView(generics.CreateAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    permission_classes = [TradePointPermission, VisitPointPermission]

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        data = {'pk': serializer.data.get('id'), 'date': serializer.data.get('date')}
        return Response(data, status=status.HTTP_201_CREATED, headers=headers)


class VisitList(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitDetailView(generics.RetrieveAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer


class VisitSearchTradePointView(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer
    
    def get_queryset(self):
        queryset = Visit.objects.all()
        name = self.kwargs.get('tradepoint')
        if name is not None:
            queryset = queryset.filter(trade_point__name=name)
            if queryset: return queryset
        raise NotFound(detail=f"Error 404, visits for this trade point - {name} not found", code=404)


class VisitSearchWorkerView(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def get_queryset(self):
        queryset = Visit.objects.all()
        name = self.kwargs.get('worker')
        if name is not None:
            queryset = queryset.filter(trade_point__worker__name=name)
            if queryset: return queryset
        raise NotFound(detail=f"Error 404, visits for this worker - {name} not found", code=404)


class SearchByParameters(generics.ListAPIView):
    queryset = Visit.objects.all()
    serializer_class = VisitSerializer

    def get_queryset(self):
        queryset = Visit.objects.all()
        worker = self.request.query_params.get('worker') 
        trade_point = self.request.query_params.get('tradepoint')
        if worker:
            queryset = queryset.filter(trade_point__worker__name=worker)
            if queryset: return queryset
        elif trade_point:
            queryset = queryset.filter(trade_point__name=trade_point)
            print(queryset)
            if queryset: return queryset
        raise NotFound(detail=f"Error 404, visit for this query not found", code=404)
        