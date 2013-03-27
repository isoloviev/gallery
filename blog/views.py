from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.db import connection
from django.shortcuts import render
from blog.models import Post
from isoloviev.utils import dictfetchall


def index(request, tagName=None):
    if tagName:
        posts = Post.objects.all().filter(tags__name=tagName).order_by('-pubDate')
    else:
        posts = Post.objects.all().order_by('-pubDate')

    paginator = Paginator(posts, 10)
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    try:
        fp = paginator.page(page)
    except (EmptyPage, InvalidPage):
        fp = paginator.page(paginator.num_pages)

    cursor = connection.cursor()
    cursor.execute("""
        SELECT
            bt.name, COUNT( bpt.tag_id ) cnt
        FROM
            blog_tag bt
            LEFT JOIN blog_post_tags bpt ON bt.id = bpt.tag_id
        GROUP BY
            name
        ORDER BY
            cnt DESC""")
    tags = dictfetchall(cursor)

    return render(request, 'blog/index.html', {'posts': fp, 'tags': tags})


def read(request, post_id):
    post = Post.objects.get(id=post_id)
    return render(request, 'blog/read.html', {'post': post})