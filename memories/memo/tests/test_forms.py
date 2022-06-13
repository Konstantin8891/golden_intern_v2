from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.test import Client, TestCase
from django.urls import reverse

from ..forms import InMemoriesForm
from ..models import InMemories

User = get_user_model()


class InMemoriesCreateFormTests(TestCase):

    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test')
        cls.form = InMemoriesForm()
        cls.memo_count = InMemories.objects.count()
        cls.post_data = {
            'user': cls.user,
            'title': 'Заголовок',
            'comment': 'Текст',
            'location': Point(0, 0)
        }

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_create_post(self):
        self.authorized_client.post(
            reverse('memo:create'),
            data=self.post_data
        )
        self.assertEqual(InMemories.objects.count(), self.memo_count + 1)
        self.assertTrue(InMemories.objects.filter(
            title='Заголовок',
            comment='Текст',
            user=self.user,
            location=Point(0, 0)
        ).exists())
