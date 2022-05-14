from django.urls import reverse
from django.test import TestCase, Client

from .models import Worker


c = Client()

class NewsTest(TestCase):

    def setUp(self):
        worker = Worker(name='test', phone='123')
        worker.save()
    
    def test_setup_user_count(self):
        user_count = Worker.objects.count()
        self.assertEqual(user_count, 1)

    def test_all_urls(self):
        worker_list = reverse('worker-list')
        response = self.client.get(worker_list)
        self.assertTrue(response.status_code == 200)