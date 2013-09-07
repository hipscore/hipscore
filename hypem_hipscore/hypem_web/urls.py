from django.conf.urls import patterns, include, url

urlpatterns = patterns('hypem_web.views',
                       url(r'^$', 'index',name="index"),
                   )
