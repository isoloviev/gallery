from django.conf.urls import patterns, include, url

from django.contrib import admin
from isoloviev import settings

admin.autodiscover()

urlpatterns = patterns('',
                       # Examples:
                       url(r'^$', 'isoloviev.views.home', name='home'),
                       url(r'^contacts/$', 'isoloviev.views.contacts'),
                       url(r'^about/$', 'isoloviev.views.about'),
                       # url(r'^isoloviev/', include('isoloviev.foo.urls')),

                       url(r'^blog/$', 'blog.views.index', name='blog-index'),
                       url(r'^blog/(\d+)/$', 'blog.views.read', name='blog-details'),
                       url(r'^blog/tags/(.+)/$', 'blog.views.index'),

                       url(r'^photo/$', 'photo.views.index'),

                       # Uncomment the admin/doc line below to enable admin documentation:
                       url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

                       # Uncomment the next line to enable the admin:
                       url(r'^admin/', include(admin.site.urls)),

                       (r'^ckeditor/', include('ckeditor.urls')),
)

if settings.DEBUG:
    urlpatterns += patterns('',
                            url(r'^media/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.MEDIA_ROOT,
                            }),
                            url(r'^static/(?P<path>.*)$', 'django.views.static.serve', {
                                'document_root': settings.STATIC_ROOT,
                            }),
    )