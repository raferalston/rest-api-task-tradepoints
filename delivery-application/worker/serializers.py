from rest_framework import serializers

from .models import Worker


class WorkerSerializer(serializers.ModelSerializer):
    tradingpoints = serializers.PrimaryKeyRelatedField(many=True, read_only=True)
    highlight = serializers.HyperlinkedIdentityField(view_name='worker-detail', format='json')
    
    class Meta:
        model = Worker
        fields = ['id', 'name', 'phone', 'tradingpoints', 'highlight']

