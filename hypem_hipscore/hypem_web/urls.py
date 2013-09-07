from django.conf.urls import patterns, include, url

urlpatterns = patterns('hypem_web.views',
                       url(r'^$', 'index',name="index"),



                       #endpoints for the frontend
                       url(r'^favorites/(?P<username>.*)/$', 'favorites',name="favorites"),
                       url(r'^popular/$', 'popular',name="popular"),
                   )
