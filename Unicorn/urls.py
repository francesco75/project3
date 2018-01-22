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
#from ticket import views
from home import views
from ticket import views as ticket_views
from vote import views as vote_views
from Payment import views as Payment_views
from charts import views as charts_views


urlpatterns = [
    ################### AUTHENTICATION ###############

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', views.get_index),
    url(r'^home/$', views.get_index),
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

    url(r'^(?P<id>\d+)/vote/$', vote_views.create_vote, name='create_vote'),

    ################# Feature Pay #####################

    url(r'^(?P<id>\d+)/payment_form/$', Payment_views.payment_form, name='payment_form'),
    url(r'^payments/(?P<id>\d+)/$', Payment_views.payment_detail, name='payment_detail'),
    url(r'^paypal-return/$', Payment_views.payment_finish, name='paypal-return'),
    url(r'^(?P<id>\d+)cancel/$', Payment_views.paypal_cancel, name = 'cancel'),

  ##################### Chart ##########################
    url(r'^charts/$', charts_views.charts, name='charst'),
    url(r'^chart-data/$', charts_views.chart_data, name='chart_data'),
    url(r'^chart-vote/$', charts_views.chart_vote, name='chart_vote'),
]