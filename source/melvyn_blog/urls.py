from django.conf.urls import url
from . import views


urlpatterns = [
    url(r'^$', views.home, name='home'),
    url(r'^posts/$', views.posts, name='posts'),
    url(r'^(?P<pk>\d+)/$', views.post, name='post'),
    url(r'^about/$', views.about, name='about'),
    url(r'^contact/$', views.contact, name='contact'),
]
