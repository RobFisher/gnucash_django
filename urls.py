from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'gnucash_django.views.index', name='index'),
    url(r'^account/(?P<full_name>[^/]+)/', 'gnucash_django.views.account', name='account'),
    )
