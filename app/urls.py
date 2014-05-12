from django.conf.urls import patterns, include, url
from django.conf import settings
from app import views


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',

    #======== angular home ==================
    url(r'^$', 'app.views.home', name="home"),


    #======== rest framework urls ==============

    #url(r'^api-auth/', include('rest_framework.urls',
    #                          namespace='rest_framework')),
    #url(r'^api/search/(?P<job>.+)[/]?$', views.SearchRest.as_view(), name="search_rest"),
    #url(r'^api/search[/]?$', views.SearchRest.as_view(), name="search_rest"),
    #url(r'^api/stay/(?P<job>.+)/(?P<site>.+)[/]?$', views.SearchStay.as_view(), name="search_stay"),
    #url(r'^api/messages/', views.EmailIn.as_view(), name="email_in"),
    #url(r'^api/adder/(?P<pk>[0-9]+)/$', views.AdderAdd.as_view(), name='adder-add'),
    #url(r'^api/adder/', views.AdderList.as_view(), name="adder"),


)