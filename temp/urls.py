'''
Created on Nov 16, 2013

@author: Cawb07
'''
from django.conf.urls import patterns, url
from django.views.generic import TemplateView
from temp import views

urlpatterns = patterns('',
    #url(r'^contact/', views.contact, name='contact'),
    url(r'^$', TemplateView.as_view(template_name='temp/home.html'), name="home"),
    #url(r'^about/', TemplateView.as_view(template_name='temp/about.html'), name="about"),
)