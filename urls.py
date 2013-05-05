from django.conf.urls.defaults import *

urlpatterns = patterns('',
    url(r'^$', 'gnucash_django.views.index', name='index'),
    )

