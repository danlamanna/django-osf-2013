from django.conf.urls import patterns, include, url
from main.views import tasks_view

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
#                       url(r'^tasks$', 'django_osf_2a013.views.tasks_view'),
    # url(r'^django_osf_2013/', include('django_osf_2013.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('main.views',
                        url(r'^tasks$', 'tasks_view'),
)
