from django.conf.urls import include, url
from django.contrib import admin
from django.http import HttpResponse

from tracker import views

urlpatterns = [
    url(r'^$', views.entry_list, name='entry-list',),
    url(r'^add/$', views.entry_add, name='entry-add'),
    url(r'^(?P<entry_id>\d+)/$', views.entry_edit, name='entry-edit'),
    url(r'^(?P<entry_id>\d+)/stop/$', views.entry_stop, name='entry-stop'),
    url(r'^(?P<entry_id>\d+)/continue/$', views.entry_continue, name='entry-continue'),

    url(r'^admin/', include(admin.site.urls)),
]
