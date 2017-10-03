from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^$', views.start_page),
    url(r'^music/', views.music_page),

]