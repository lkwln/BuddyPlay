from django.conf.urls import patterns, include, url
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
admin.autodiscover()


def bp_url(regex, view, kwargs=None, name=None, prefix=''):
    url_prefix = '^api/v1/'
    regex = url_prefix+regex
    return url(regex, view, kwargs, name, prefix)

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'buddyplay.views.home', name='home'),
    # url(r'^buddyplay/', include('buddyplay.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    bp_url(r'auth/', include('rest_framework.urls', namespace='rest_framework')),
    bp_url(r'user/', include('bp_user.urls')),
    # bp_url(r'merchant/', include('bp_merchant.urls')),
    # bp_url(r'activity/', include('activity.urls')),
    bp_url(r'orders/', include('order_system.urls')),
    # bp_url(r'social/', include('social.urls')),
)
