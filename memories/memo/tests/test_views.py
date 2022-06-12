from django.contrib.auth import get_user_model
from django.contrib.gis.geos import Point
from django.test import Client, TestCase
from django.urls import reverse

from ..models import InMemories

User = get_user_model()


class PostPagesTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test')
        cls.memo = InMemories.objects.create(
            user=cls.user,
            title='Заголовок',
            comment='Текст',
            location=Point(0, 0)
        )
        cls.page_template = {
            reverse('memo:index'):
            'memo/index.html',
            reverse('memo:profile'):
            'memo/profile.html',
            reverse('memo:create'):
            'memo/create_post.html',
            reverse('memo:post_detail', kwargs={'post_id': cls.memo.pk}):
            'memo/post_detail.html',
        }
        cls.memo_data = {
            'title': 'Заголовок1',
            'comment': 'Текст1',
            'location': Point(1, 1)
        }

    def setUp(self):
        self.authorized_client = Client()
        self.authorized_client.force_login(self.user)
        self.guest_client = Client()

    def test_pages_names(self):
        for page, template in self.page_template.items():
            with self.subTest(page=page):
                response = self.authorized_client.get(page)
                self.assertTemplateUsed(response, template)

    def test_editable_context(self):
        rev = reverse('memo:create')
        with self.subTest(rev=rev):
            response = self.authorized_client.get(rev)
            self.assertIn('form', response.context)

    # тест контекста profile
    def test_correct_read_only_context(self):
        rev = reverse('memo:profile')
        with self.subTest(rev=rev):
            response = self.authorized_client.get(rev)
            first_object = response.context['posts'][0]
            post_user = first_object.user
            post_title = first_object.title
            post_comment = first_object.comment
            post_location = first_object.location
            self.assertEqual(post_user, self.memo.user)
            self.assertEqual(post_title, self.memo.title)
            self.assertEqual(post_comment, self.memo.comment)
            self.assertEqual(post_location, self.memo.location)

    # Тест контекста post_detail
    def test_post_detail_context(self):
        response = self.authorized_client.get(reverse(
            'memo:post_detail',
            kwargs={'post_id': self.memo.pk})
        )
        post_obj = response.context['post']
        post_user = post_obj.user
        post_title = post_obj.title
        post_comment = post_obj.comment
        post_location = post_obj.location
        self.assertEqual(post_user, self.memo.user)
        self.assertEqual(post_title, self.memo.title)
        self.assertEqual(post_comment, self.memo.comment)
        self.assertEqual(post_location, self.memo.location)

    # Тест создания поста
    def test_post_create(self):
        self.authorized_client.post(
            reverse('memo:create'),
            data=self.memo_data,
            follow=True,
        )
        rev = reverse('memo:profile')
        with self.subTest(rev=rev):
            response = self.authorized_client.get(rev)
            first_object = response.context['posts'][0]
            post_user = first_object.user
            post_title = first_object.title
            post_comment = first_object.comment
            post_location = first_object.location
            self.assertEqual(post_user, self.memo.user)
            self.assertEqual(post_title, self.memo.title)
            self.assertEqual(post_comment, self.memo.comment)
            self.assertEqual(post_location, self.memo.location)
