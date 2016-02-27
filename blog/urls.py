from django.conf.urls import patterns, url
from django.views.generic import ListView
from blog.models import Post

pag_num = 3

urlpatterns = patterns('',
    # Index
    #url('^$', ListView.as_view(model=Post, 
                               #template_name='templates/post_list.html',
                               #paginate_by=pag_num,
                               #)),
    
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(model=Post,
                                                template_name='templates/post_list.html',
                                                paginate_by=pag_num), name='index'),    
    
)