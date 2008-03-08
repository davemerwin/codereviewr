from django.conf.urls.defaults import *
from code.views import next_works
from openid_cr.views import begin, complete, signout
from django.views.generic.simple import direct_to_template, redirect_to
from codereviewr.settings import DEBUG
import os

urlpatterns = patterns('',
    (r'^code/', include('codereviewr.code.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^next-works/$', next_works),
     
    #for homepage - testing
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
)

if DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': os.path.expanduser('~/git/codereviewr/media')}),
    )
