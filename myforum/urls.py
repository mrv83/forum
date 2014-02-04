from django.conf.urls import patterns, url
from myforum import views

urlpatterns = patterns('',
    url(r'^newthemes/$', 'myforum.views.create_new_theme', name='new_theme'),
#    url(r'^forum/$', 'myforum.views.forum_view', name='forum_form'),
    url(r'^themelist/$', 'myforum.views.themelist', name='list_themes'),
    url(r'^theme/(?P<themes_id>\d+)/$', 'myforum.views.choose_themes', name='choozen_theme'),
    # url(r'^setsmiles/','myforum.views.setsmiles', name='setupsmiles'),
    # url(r'^setsmiles/(?P<iconsmiles_id>\d+)/$', 'myforum.views.smileitem_edit', name='smileitem_edit'),
    # url(r'^newsetsmiles/','myforum.views.newsetsmiles', name='newsetupsmiles'),
    # url(r'^delsmiles/','myforum.views.delsmiles', name='delsmiles'),
    # url(r'^addsmiles/','myforum.views.addsmiles', name='addsmiles'),
)