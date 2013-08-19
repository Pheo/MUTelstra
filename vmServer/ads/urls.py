from django.conf.urls import patterns, url

from ads import views 

urlpatterns = patterns ('',
	# ex: /
	url(r'^$', views.index, name='index'),
	url(r'^(?P<ad_id>\d+)/$', views.display, name='display'),	
)
