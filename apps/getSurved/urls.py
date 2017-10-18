from django.conf.urls import url
from . import views
urlpatterns = [
    url(r'^process$', views.process),
    url(r'^refresh$', views.refresh),
    url(r'^$', views.index),
    url(r'^result$', views.result)
    
]