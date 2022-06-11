from django.test import TestCase
from django.contrib.auth import get_user_model

from ..models import InMemories 


class InMemoriesModelTest(TestCase):
    @classmethod
    def setUpClass(cls):
        super().setUpClass()
        cls.user = User.objects.create_user(username='test')
        cls.memo = InMemories.objects.create(
            title='Заголовок',
            comment='Текст',
            location=(0 0)
        )

    def test_verbose_name(self):
        memo = InMemoriesModelTest.memo
        field_verboses = {
            'title': 'Заголовок',
            'comment': 'Воспоминание',
       }
        for field, expected_value in field_verboses.items():
            with self.subTest(field=field):
                self.assertEqual(
                    memo._meta.get_field(field).verbose_name, expected_value)

    def test_help_text(self):
        memo = InMemoriesModelTest.memo
        field_help_texts = {
            'title': 'Введите название воспоминания',
            'comment': 'Введите текст воспоминания',
        }
        for field, expected_value in field_help_texts.items():
            with self.subTest(field=field):
                self.assertEqual(
                    task._meta.get_field(field).help_text, expected_value) 