from django.conf.urls import patterns, url

from rany import views

urlpatterns = patterns('',
	url(r'^$', views.index, name= 'index'),
	url(r'^/inscribete/', views.inscribete, name = 'inscribete'),
)