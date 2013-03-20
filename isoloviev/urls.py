from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'isoloviev.views.home', name='home'),
    url(r'^contacts/$', 'isoloviev.views.contacts'),
    url(r'^about/$', 'isoloviev.views.about'),
    # url(r'^isoloviev/', include('isoloviev.foo.urls')),

    url(r'^blog/$', 'isoloviev.views.home'),

    url(r'^photo/$', 'photo.views.index'),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
