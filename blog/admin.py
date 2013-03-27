from django.contrib import admin
from blog.models import Post, Tag


class PostAdmin(admin.ModelAdmin):
    list_display = ('pubDate', 'title')
    list_filter = ('pubDate',)
    ordering = ('-pubDate',)

admin.site.register(Post, PostAdmin)
admin.site.register(Tag)

