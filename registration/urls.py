from django.conf.urls import patterns, url
from registration.views import login, logout
from registration import views, forms

urlpatterns = patterns('',
    url(r'^reg_user/$', 'registration.views.reg_new_user', name='registr_user'),
    url(r'^login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^profile/$', 'registration.views.profile', name='profile'),
)