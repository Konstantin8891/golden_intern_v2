from http import HTTPStatus

from django.contrib.auth import get_user_model
from django.test import TestCase, Client
from django.contrib.gis.geos import Point

from ..models import InMemories

User = get_user_model()


class InMemoriesURLTests(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        # Создадим запись в БД для проверки доступности адреса task/test-slug/
        cls.user = User.objects.create_user(username='test')
        cls.memo = InMemories.objects.create(
            user = cls.user,
            title='Заголовок',
            comment='Текст',
            location=Point(0, 0)
        )
        cls.url_status = {
            '/unexisting_page': HTTPStatus.NOT_FOUND,
            '/': HTTPStatus.OK,
            '/accounts/profile/': HTTPStatus.FOUND,
            '/create_post/': HTTPStatus.FOUND,
            f'/posts/{cls.memo.pk}/': HTTPStatus.FOUND,
        }
        cls.urls = [
            '/accounts/profile/',
            '/create_post/',
            f'/posts/{cls.memo.pk}/',
        ]
        cls.url_template = {
            '/': 'memo/index.html',
            '/accounts/profile/': 'memo/profile.html',
            f'/posts/{cls.memo.pk}/': 'memo/post_detail.html',
            '/create_post/': 'memo/create_post.html',
        }


    def setUp(self):
        self.guest_client = Client()
        # self.user = User.objects.create_user(username='test')
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)

    def test_guest_client(self):
        for address, status in self.url_status.items():
            with self.subTest(address=address):
                response = self.guest_client.get(address)
                self.assertEqual(response.status_code, status)

    def test_authorized_user(self):
        for url in self.urls:
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_templates(self):
        for url, template in self.url_template.items():
            with self.subTest(url=url):
                response = self.authorized_client.get(url)
                self.assertTemplateUsed(response, template)