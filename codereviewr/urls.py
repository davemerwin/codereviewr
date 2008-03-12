from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to
from codereviewr.settings import PROJECT_PATH, DEBUG
import os

urlpatterns = patterns('',
    (r'^code/', include('codereviewr.code.urls')),
    
    # Admin
    (r'^admin/code/language/refresh/$', 'code.views.refresh_languages'),
    (r'^admin/', include('django.contrib.admin.urls')),
     
    #for homepage - testing
    (r'^$', direct_to_template, {'template': 'homepage.html'}),
)

if DEBUG:
    urlpatterns += patterns('', 
        (r'^media/(.*)$', 'django.views.static.serve', {'document_root': '%s/../media' % (PROJECT_PATH)})
    )
