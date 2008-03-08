from django.conf.urls.defaults import *

urlpatterns = patterns('codereviewr.code.views',
    # Writes
    url(r'^(?P<code_id>\d+)/', 'code_detail', name='code_detail'),
)
