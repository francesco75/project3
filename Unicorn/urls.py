"""Unicorn URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.8/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import  include, url
from django.contrib import admin

from accounts import views as accounts_views
from accounts.views import register,profile, login, logout
from ticket import views
from home import views
from ticket import views as ticket_views



urlpatterns = [
    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.get_index),
    url(r'^register/$', accounts_views.register, name='register'),
    url(r'^profile/$', accounts_views.profile, name='profile'),
    url(r'^login/$', accounts_views.login, name='login'),
    url(r'^logout/$', accounts_views.logout, name='logout'),

    ############# C R U D ###############

    url(r'^ticket/create/$', ticket_views.create_ticket, name='create_ticket'),
    url(r'^ticket/list/$', ticket_views.tickets_list, name='tickets_list'),
    url(r'^(?P<id>\d+)/$',ticket_views.ticket_detail, name='ticket_detail'),
    url(r'^(?P<id>\d+)edit/$', ticket_views.edit_ticket, name='edit'),
    url(r'^(?P<id>\d+)delete/$', ticket_views.delete_ticket, name='delete'),

    ################# Vote ###############
    url(r'^create_vote/$', ticket_views.create_vote, name='create_vote'),
    url(r'^vote/list/$', ticket_views.vote_list, name='vote_list'),


]