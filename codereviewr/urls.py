from django.conf.urls.defaults import *

urlpatterns = patterns('',
    (r'^code/', include('codereviewr.code.urls')),
    (r'^admin/', include('django.contrib.admin.urls')),
)
