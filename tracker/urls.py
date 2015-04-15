from django.conf.urls import include, url

from . import views


urlpatterns = [
    url(r'^entry/$', views.entry_list, name='entry-list'),
    url(r'^entry/add/$', views.entry_add, name='entry-add'),
    url(r'^entry/(?P<entry_id>\d+)/$', views.entry_edit, name='entry-edit'),
]
