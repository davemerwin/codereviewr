from django.conf.urls.defaults import *
from code.views import next_works
from openid_cr.views import begin, complete, signout

urlpatterns = patterns('',
    (r'^admin/', include('django.contrib.admin.urls')),
    (r'^next-works/$', next_works),
)
