from django.db import models
from django.utils.text import slugify


# Create your models here.

class Post(models.Model):
    """Post - individual post eg. blog entry"""
    title = models.TextField("Post Title", max_length=300)
    author = models.TextField("Author", max_length=100, default="schlerp")
    pub_date = models.DateTimeField("Publishing Date", auto_now=True)
    text = models.TextField("Body")
    slug = models.SlugField(max_length=40, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)
    
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


class Media(models.Model):
    """This represents a peice of media.. most likely just pictures.."""
    title = models.TextField("Media Title", max_length=100)
    upload = models.FileField(upload_to='uploads/')
    slug = models.SlugField(max_length=50, unique=True, null=True)
    
    def save(self, *args, **kwargs):
        self.slug = slugify(self.title)
        super(Media, self).save(*args, **kwargs)