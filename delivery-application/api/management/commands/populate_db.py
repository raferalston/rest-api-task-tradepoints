from django.core.management.base import BaseCommand, CommandError
from tradepoint.models import TradePoint, Visit
from worker.models import Worker

class Command(BaseCommand):
    help = 'Populate some db data'

    def random_name(self, num):
        from random import choice
        first_names = ('Batman', 'Superman', 'Amazingman')
        last_names = ('Whoknows', 'Nobody', 'Somename')
        return f'{num} {choice(first_names)} {choice(last_names)}'

    def random_phone(self):
        from random import randint
        return f'{randint(100000, 999999)}'

    def handle(self, *args, **options):
        self.stdout.write(self.style.SUCCESS('Begin populating db'))
        workers = []
        for i in range(10):
            worker = Worker.objects.create(name=self.random_name(i), phone=self.random_phone())
            workers.append(worker)
        
        for i, w in enumerate(workers):
            TradePoint.objects.create(name=i, worker=workers[i])

        self.stdout.write(self.style.SUCCESS('Done populating db'))