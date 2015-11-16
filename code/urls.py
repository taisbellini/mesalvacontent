from django.conf.urls import patterns, url
from django.conf import settings
import views

urlpatterns = patterns('',
                            url(r'^$', views.index, name="index"),
                            url(r'^actions/$', views.actions, name="actions"),
                            (r'^(?P<path>(?:img|css|js|text|static|fonts|other)/.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       )