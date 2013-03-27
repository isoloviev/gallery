from django.db import models
from ckeditor.fields import RichTextField
from comments.models import Comment


class Tag(models.Model):
    name = models.CharField(max_length=250)

    def __unicode__(self):
        return self.name


class Post(models.Model):
    pubDate = models.DateTimeField()
    title = models.CharField(max_length=250)
    content = RichTextField()
    comments = models.ManyToManyField(Comment, blank=True, null=True, )
    tags = models.ManyToManyField(Tag, blank=True, null=True, )

    def _get_short_content(self):
        if self.content.__contains__('<hr />') > 0:
            return self.content[:self.content.index('<hr />')]
        else:
            return self.content

    shortContent = property(_get_short_content)

    def _get_full_content(self):
        return self.content.replace('<hr />', '')

    fullContent = property(_get_full_content)

    def _get_count_comments(self):

        return 0

    count_comments = property(_get_count_comments)

    def __unicode__(self):
        return self.title