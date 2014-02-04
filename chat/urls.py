from django.conf.urls import patterns, url

urlpatterns = patterns('',
    url(r'^$', 'chat.views.chat', name='chat'),
    url(r'^create_channel/$', 'chat.views.create_channel', name='create_channel'),
    url(r'^channel_list/$', 'chat.views.channel_list', name='channel_list'),
    url(r'^channel/(?P<channel>\d+)/$', 'chat.views.channel_X', name='channel_X'),
    url(r'^add/$', 'chat.views.add_message', name='add_message'),
)
