from django.conf.urls import url
from tasks.views import *
# app_name = 'tasks'
urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^task/([0-9]+)?/$', task, name='task'),
    url(r'^tasks/$', tasks, name='tasks'),
    url(r'^profile/([0-9]+)?/$', profile, name='profile'),
    url(r'^create_task/$', create_task, name='create_task'),
    url(r'^people/$', people, name='people'),
    url(r'^(?P<url>about/)$', 'django.contrib.flatpages.views.flatpage'),
]
