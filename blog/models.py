from django.db import models
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    """Post - individual post eg. blog entry"""
    title = models.TextField("Post Title", max_length=300)
    author = models.TextField("Author", max_length=100, default="Schlerp")
    pub_date = models.DateTimeField("Publishing Date", auto_now=True)
    text = models.TextField("Body")
    slug = models.SlugField(max_length=40, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
    
    def get_absolute_url(self):
        return "/%s/%s/%s/" % (self.pub_date.year, self.pub_date.month, self.slug)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-pub_date"]

class Comment(models.Model):
    """Comment - Individual comment, each post may have many"""
    author = models.TextField("Author", max_length=100, default="Anonymous")
    pub_date = models.DateTimeField("Publish Date", auto_now=True)
    post = models.ForeignKey(Post)
