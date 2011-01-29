from django.conf.urls.defaults import *

urlpatterns = patterns('blog.views',
    ('^$', 'index'),
)