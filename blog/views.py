from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader, RequestContext
from blog.models import Post

from blog.forms import UploadFileForm
from blog.utils import handle_uploaded_file

# Create your views here.

def test(request):
    template = loader.get_template('templates/base.html')
    post = Post()
    post.title = "derp"
    post.pub_date = "1/1/2016"
    post.text = "derp herp schelrp"
    post.authot = "schlerp"
    context = RequestContext(request, [post,])
    return HttpResponse(template.render(context))

def create_post(request):
    template = loader.get_template('templates/create_post.html')
    context = RequestContext(request)
    return HttpResponse(template.render(context))

def home(request):
    return HttpResponse("chicken sandwich")

def upload_file(request):
    if request.method == 'POST':
        form = UploadFileForm(request.POST, request.FILES)
        if form.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponseRedirect('/success/url/')
    else:
        form = UploadFileForm()
    return render(request, 'upload.html', {'form': form})
