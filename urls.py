from django.conf.urls.defaults import *
from django.contrib import admin
import dbindexer
from temp import views
from django.views.generic import TemplateView

handler500 = 'djangotoolbox.errorviews.server_error'

# django admin
admin.autodiscover()

# search for dbindexes.py in all INSTALLED_APPS and load them
dbindexer.autodiscover()

urlpatterns = patterns('',
    ('^$', include('temp.urls')),
    url('^contact/$', TemplateView.as_view(template_name='temp/contact.html'), name='contact'),
    url('^about/$', TemplateView.as_view(template_name='temp/about.html'), name="about"),
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    #('^$', 'django.views.generic.simple.direct_to_template', {'template': 'home.html'}),
    ('^admin/', include(admin.site.urls)),
)
