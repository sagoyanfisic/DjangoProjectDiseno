from django.conf.urls.defaults import patterns, include, url
# Uncomment the next two lines to enable the admin:
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'ProjectEstadio.views.home', name='home'),
    # url(r'^ProjectEstadio/', include('ProjectEstadio.foo.urls')),
    #url(r'^$,'principal.views.lista_bedidas'^admin/',),
    #url(r'^$','principal.views.lista_bebidas'),
    url(r'^$','principal.views.lista_bebidas'),
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),

)
