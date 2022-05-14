from django.db import models

from worker.models import Worker


class TradePoint(models.Model):
    class Meta:
        verbose_name = 'Trade point'
        verbose_name_plural = 'Trade points'

    def __str__(self):
        return self.name

    name = models.CharField(max_length=255)
    worker = models.ForeignKey(Worker, related_name='tradingpoints', on_delete=models.CASCADE)
    

class Visit(models.Model):
    class Meta:
        verbose_name = 'Visit'
        verbose_name_plural = 'All visits'

    def __str__(self):
        return self.trade_point.name

    date = models.DateTimeField(auto_now=True)
    trade_point = models.ForeignKey(TradePoint, related_name='tradepoints', on_delete=models.CASCADE)
    latitude = models.FloatField()
    longitude = models.FloatField()