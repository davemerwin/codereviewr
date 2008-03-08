from django.conf.urls.defaults import *
from codereviewr.code.views import code_list, code_detail

urlpatterns = patterns('',
    url(r'^$', code_list, name='code_list'),
    url(r'^(?P<code_id>\d+)/$', code_detail, name='code_detail'),
)
