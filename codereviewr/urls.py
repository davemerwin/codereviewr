from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from codereviewr.settings import PROJECT_PATH, DEBUG
from codereviewr.feeds import *
#from django.contrib.comments.feeds import *
import os

#feeds dictionary
feeds = {
	'user': UserFeed,
	'comments':LatestComments,
}

urlpatterns = patterns('',
    (r'^code/', include('codereviewr.code.urls')),
    
    # Admin
    (r'^admin/code/language/refresh/$', 'code.views.refresh_languages'),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^openid/$', 'openid_cr.views.begin', {'redirect_to': '/openid/complete/'}),
    (r'^openid/complete/$', 'openid_cr.views.complete'),
    (r'^openid/signout/$', 'openid_cr.views.signout'),
    
    #for homepage - testing
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
	
    (r'^feeds/(?P<url>.*)/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
)

if DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (PROJECT_PATH)})
    )
