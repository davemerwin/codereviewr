from django.conf.urls.defaults import patterns

urlpatterns = patterns('',
    (r'^$', 'django_openidconsumer.views.begin'),
    (r'^logo/$', 'django_openidconsumer.views.logo'),
    (r'^signout/$', 'django_openidconsumer.views.signout'),
    (r'^complete/$', 'django_openidconsumer.views.complete'),

    
)
