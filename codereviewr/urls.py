from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from codereviewr.settings import PROJECT_PATH, DEBUG
from codereviewr.feeds import *
import os

#feeds dictionary
feeds = {
	'latest': LatestEntries,
}

urlpatterns = patterns('',
    (r'^code/', include('codereviewr.code.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
	(r'^feeds/(?P<url>.*/$', 'django.contrib.syndication.views.feed', {'feed_dict': feeds}),
    #for homepage - testing
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
)

if DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (PROJECT_PATH)})
    )
