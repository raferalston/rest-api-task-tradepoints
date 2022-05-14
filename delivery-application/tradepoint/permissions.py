from rest_framework import permissions

from worker.models import Worker
from .models import TradePoint


class TradePointPermission(permissions.BasePermission):
    """
    Custom permission for only correct phone number of worker.
    """
    message = 'This worker is not allowed.'

    def has_permission(self, request, view):
        status = False
        param = request.query_params.get('phone') or request.POST.get('phone')
        status = Worker.objects.filter(phone=param).exists()
        return status


class VisitPointPermission(permissions.BasePermission):
    """
    Custom permission for checking worker on specific trading point.
    """
    message = 'This worker is not allowed.'

    def has_permission(self, request, view):
        status = False

        if request.method == "POST":
            param = request.POST.get('phone')
            pk = request.POST.get('trade_point')
            worker = Worker.objects.get(phone=param)
            status = TradePoint.objects.filter(pk=pk).filter(worker=worker).exists()

        return status
