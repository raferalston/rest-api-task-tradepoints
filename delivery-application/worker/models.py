from django.db import models


class Worker(models.Model):
    class Meta:
        verbose_name = 'Worker'
        verbose_name_plural = 'Workers'
    
    def __str__(self):
        return self.name
        
    name = models.CharField(max_length=255)
    phone = models.CharField(max_length=255, unique=True)