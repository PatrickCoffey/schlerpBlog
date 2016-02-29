from django.contrib import admin

from blog.models import Post, Comment, Media


# Register your models here.

class PostAdmin(admin.ModelAdmin):

    prepopulated_fields = {"slug": ("title",)}

admin.site.register(Post, PostAdmin)
#admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Media)