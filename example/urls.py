from django.conf.urls.defaults import *
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    url(r'^changer/', include(admin.site.urls)),
)

urlpatterns += patterns('django.views.generic',
    url(r'^robots\.txt$', 'simple.direct_to_template', {'template': 'robots.txt'}),
    url(r'^humans\.txt$', 'simple.direct_to_template', {'template': 'humans.txt'}),
    url(r'^html$', 'simple.direct_to_template', {'template': 'html.html'}),
)