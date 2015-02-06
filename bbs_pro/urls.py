from django.conf.urls import patterns, include, url
from django.contrib import admin
from app01 import views

admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'bbs_pro.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.index),
    url(r'^detail/(\d+)/$', views.bbs_detail),
    url(r'^sub_comment/$', views.sub_comment),
    url(r'^acc_login/$',views.account_login),
    url(r'^logout_views/$', views.logout_views),
    url(r'^login',views.login),
    url(r'^pub/',views.pub),
    url(r'^bbs_sub/',views.bbs_sub),
)

    