from django.urls import path

from . import  views

app_name = 'app'

urlpatterns = [
    path('payment', views.view_that_asks_for_money),
    path('returnpage', views.view_return,name='returnpage'),
    path('cancelpage', views.view_cancel,name='cancelpage'),
]