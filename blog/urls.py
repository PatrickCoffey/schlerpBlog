from django.conf.urls import patterns, url
from django.views.generic import ListView, DetailView
from blog.models import Post

pag_num = 3

urlpatterns = patterns('',

    # Index
    url(r'^(?P<page>\d+)?/?$', ListView.as_view(model=Post,
                                                template_name='templates/post_list.html',
                                                paginate_by=pag_num), name='index'),    
    
    # Individual posts
    url(r'^(?P<pub_date__year>\d{4})/(?P<pub_date__month>\d{1,2})/(?P<slug>[a-zA-Z0-9-]+)/?$', 
        DetailView.as_view(model=Post,
                           template_name='templates/post_detail.html'), name='post'),
)