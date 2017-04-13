from django.conf.urls import url
from . import views

# app_name = 'tasks'
urlpatterns = [
    url(r'^$', views.index, name='index'),
    url(r'^task/([0-9]+)?/$', views.task, name='task'),
    url(r'^tasks/$', views.tasks, name='tasks'),
    url(r'^profile/([0-9]+)?/$', views.profile, name='profile'),
    url(r'^people/$', views.people, name='people'),
]