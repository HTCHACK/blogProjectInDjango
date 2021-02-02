from django.contrib import admin
from django.contrib.admin.helpers import AdminErrorList
from blogapp.models import Category, BlogComment, Contact, Contact, News, Post, Subscribe
# Register your models here.

admin.site.register(Category)
admin.site.register(Contact)
admin.site.register(BlogComment)
admin.site.register(Subscribe)

@admin.register(News)
class NewsAdmin(admin.ModelAdmin):
    class Media:
        js = ('news.js',)

@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    class Media:
        js = ('post.js',)





