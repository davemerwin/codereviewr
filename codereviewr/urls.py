from django.conf.urls.defaults import *
from django.views.generic.simple import direct_to_template, redirect_to

urlpatterns = patterns('',
     (r'^admin/', include('django.contrib.admin.urls')),
     
     #for homepage - testing
     (r'^$', direct_to_template, {'template': 'homepage.html'}),
     
)
