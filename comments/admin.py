from django.contrib import admin
from comments.models import Author, Comment


class CommentAdmin(admin.ModelAdmin):
    list_display = ('pubDate', 'subject')
    list_filter = ('author',)
    ordering = ('-pubDate',)


admin.site.register(Comment, CommentAdmin)
admin.site.register(Author)
