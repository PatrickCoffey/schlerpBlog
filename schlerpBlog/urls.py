from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'schlerpBlog.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    # for testing purposes
    url(r'^test/', 'blog.views.test', name='test'),

    url(r'^admin/', include(admin.site.urls)),
    
    #url(r'^blog/', include('blog.urls')),
    url(r'^.*$', include('blog.urls')),
)
