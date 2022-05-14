from rest_framework import serializers

from .models import TradePoint, Visit


class TradePointSerializer(serializers.ModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='tradepoint-detail', format='json')

    class Meta:
        model = TradePoint
        fields = ['id', 'name', 'worker', 'highlight']

class WorkerTradepointSerializer(serializers.ModelSerializer):

    class Meta:
        model = TradePoint
        fields = ['id', 'name']

class VisitSerializer(serializers.ModelSerializer):
    highlight = serializers.HyperlinkedIdentityField(view_name='visit-detail', format='json')

    class Meta:
        model = Visit
        fields = ['id', 'date', 'trade_point', 'latitude', 'longitude', 'highlight']
