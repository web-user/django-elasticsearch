from django.urls import path, include
from django.contrib.auth.views import login
from django.contrib.auth.views import logout
from django.contrib.auth.views import logout_then_login
from rest_framework.urlpatterns import format_suffix_patterns
from django.conf.urls import handler404, handler500

from search import views


urlpatterns = [
    path('search/', views.search_views, name='search'),

]

app_name = 'search'



urlpatterns = format_suffix_patterns(urlpatterns)