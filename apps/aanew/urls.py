from django.conf.urls.defaults import *

urlpatterns = patterns('aanew.views',
    (r'^$', 'list_links'),
    (r'^submit_link/', 'submit_link'),
    url(r'^follow/(?P<link_id>\d+)/', 'follow_link', name='follow_link'),
)
