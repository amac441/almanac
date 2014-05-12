from django.conf.urls import patterns, include, url
from django.views.generic import TemplateView
from django.contrib import admin

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', TemplateView.as_view(template_name="landing.html")),
    url(r'^thanks$', TemplateView.as_view(template_name="logins/thanks.html")),
    url(r'^grow/', include('app.urls'), name='app_home'),
    url(r'^years/', include('years.urls'), name='5years_home')

)

urlpatterns += patterns('',


    # url(r'^login/$', 'login',  #this is django.contrib.auth.views.login
    #   {'template_name': 'login.html'},
    #   name='5years_login'),

    url(r'^signup$', 'root.views.signup', name='signup'),
    url(r'^login$', 'root.views.login'),
    url(r'^auth$', 'root.views.auth_view'),
    url(r'^logout$', 'root.views.logout'),
    url(r'^loggedin$', 'root.views.loggedin'),
    url(r'^invalid$', 'root.views.invalid_login'),
    url(r'^register$', 'root.views.register_user'),

)

    # url(r'^year/', include('year.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
