from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page),
    url(r'^news/', views.news_page),
    url(r'^music/', views.music_page),
    url(r'^sport/', views.sport_page),
    url(r'^tech/', views.tech_page),
]