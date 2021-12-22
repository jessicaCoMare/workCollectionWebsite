# from django.urls import path
from django.conf.urls import url
from . import views
app_name = 'blog'

urlpatterns = [
    # path('', views.index, name='index'),
    url(r'^$', views.index, name='index'),
    url(r'^post/(?P<pk>[0-9]+)/$', views.detail, name='detail'),
    url(r'^category/(?P<category>\w+)/$', views.search_category, name='search_category'),
    url(r'^tag/(?P<tag>\w+)/$', views.search_tag, name='search_tag'),
]
