from django.conf.urls.defaults import *

from django.contrib import admin
admin.autodiscover()

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    ('^$', include('blog.urls')),
)
