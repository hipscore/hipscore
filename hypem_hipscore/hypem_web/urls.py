from django.conf.urls import patterns, include, url

urlpatterns = patterns('hypem_web.views',
                       url(r'^$', 'index',name="index"),



                       #endpoints for the frontend
                       url(r'^favorites/(?P<username>.*)/$', 'favorites',name="favorites"),
                       url(r'^popular/$', 'popular',name="popular"),
                       url(r'^user/(?P<username>.*)/$', 'user',name="user"),
                       url(r'^get-track-source/(?P<track_media_id>.*)/$','get_track_source',name="get_track_source"),
                       url(r'^.*$', 'index',name="index"),



                   )
