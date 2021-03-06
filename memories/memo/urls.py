from django.urls import path

from . import views

app_name = 'memo'

urlpatterns = [
    path(
        '',
        views.index,
        name='index'
    ),
    path(
        'accounts/profile/',
        views.profile,
        name='profile'
    ),
    path(
        'confidential/',
        views.confidential,
        name='confidential'
    ),
    path(
        'delete/',
        views.delete,
        name='delete'
    ),
    path(
        'create_post/',
        views.create,
        name='create'
    ),
    path(
        'posts/<int:post_id>/',
        views.post_detail,
        name='post_detail'
    ),
]
