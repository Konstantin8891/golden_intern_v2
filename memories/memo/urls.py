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
]
