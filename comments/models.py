from django.db import models


class Author(models.Model):
    name = models.CharField(max_length=150)
    email = models.CharField(max_length=250)

    def __unicode__(self):
        return u'%s (%s)' % (self.name, self.email)


class Comment(models.Model):
    pubDate = models.DateTimeField()
    owner = models.CharField(max_length=100)
    subject = models.CharField(max_length=250)
    text = models.TextField()
    parent = models.ForeignKey('self', blank=True, null=True, )
    author = models.ForeignKey(Author)

    @staticmethod
    def count_comments(self, ou):
        checkout_count = ou.objects.filter(parent=ou.id).count()

        for kid in ou.children.all():
            checkout_count += Comment.count_comments(kid)
        return checkout_count

    def __unicode__(self):
        return self.subject

