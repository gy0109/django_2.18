from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^index/$', views.index),  # 注册index的url
    url(r'^weather/([a-z]+)/(\d{4})/$', views.weather),  # 注册weather的url
    url(r'^weather1/(?P<city>[a-z]+)/(?P<year>\d{4})/$', views.weather1),
    url(r'^weather2/(?P<city>[a-z]+)/(?P<year>\d{4})/?', views.weather2),

    url(r'^getpostparams/$', views.get_post_params),
    url(r'^getbodyjson/$', views.get_body_json),

    url(r'^response_json/$', views.response_json),


]

