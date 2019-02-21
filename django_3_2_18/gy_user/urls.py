from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^usercookie/$', views.user_cookie),
    url(r'^getcookie/$', views.get_cookie),
    url(r'^use_session/$', views.use_session),
    url(r'^BaseUseClassView/$', views.BaseUseClassView.as_view()),


]

