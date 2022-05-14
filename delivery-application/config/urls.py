from django.contrib import admin
from django.urls import path

from api.views import api_root
from worker.views import (
    WorkerView, 
    WorkerDetailView, 
    WorkerSearchView,
)
from tradepoint.views import (
    TradePointList, 
    TradePointDetailView, 
    TradePointSearchView,
    VisitList,   
    VisitDetailView,
    VisitSearchTradePointView,
    VisitSearchWorkerView,
    WorkerTradepointView,
    WorkerVisitTradePointView,
    SearchByParameters
)

urlpatterns = [
    path('admin/', admin.site.urls),
    
    path('api/', api_root),
    path('api/tradepoints', WorkerTradepointView.as_view(), name='worker-tradepoints-list'),
    path('api/visit-trade-point', WorkerVisitTradePointView.as_view(), name='worker-visit-tradepoint'),

    path('api/admin/workers', WorkerView.as_view(), name='worker-list'),
    path('api/admin/workers/<int:pk>', WorkerDetailView.as_view(), name='worker-detail'),
    path('api/admin/workers/search/<name>', WorkerSearchView.as_view(), name='worker-search'),

    path('api/admin/tradepoints/', TradePointList.as_view(), name='tradepoint-list'),
    path('api/admin/tradepoints/<int:pk>', TradePointDetailView.as_view(), name='tradepoint-detail'),
    path('api/admin/tradepoints/search/<name>', TradePointSearchView.as_view(), name='tradepoint-search'),

    path('api/admin/visits/', VisitList.as_view(), name='visit-list'),
    path('api/admin/visits/<int:pk>', VisitDetailView.as_view(), name='visit-detail'),
    path('api/admin/visits/tradepoint-search/<tradepoint>', VisitSearchTradePointView.as_view(), name='visit-search-tradepoint-name'),
    path('api/admin/visits/worker-search/<worker>', VisitSearchWorkerView.as_view(), name='visit-search-worker-name'),

    path('api/admin/visits/search/', SearchByParameters.as_view(), name='visit-search'),
]
