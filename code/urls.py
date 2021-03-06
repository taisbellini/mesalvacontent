from django.conf.urls import patterns, url
from django.conf import settings
import views

urlpatterns = patterns('',
                            url(r'^$', views.index, name="index"),
                            url(r'^show_professor/$', views.show_professor, name="show_professor"),
			    url(r'^show_modules/(?P<pk>[0-9]+)$', views.show_modules, name="show_modules"),
			    url(r'^show_classes/(?P<pk>[0-9]+)$', views.show_classes, name="show_classes"),
                            (r'^(?P<path>(?:img|css|js|text|static|fonts|other)/.*)$', 'django.views.static.serve', {'document_root': settings.STATIC_ROOT}),
                       )
