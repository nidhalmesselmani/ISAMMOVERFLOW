from django.conf.urls import include, url
from . import views
urlpatterns = [
    #Add Django site authentication urls (for login, logout, password management
    url(r'^', include('django.contrib.auth.urls')),
    url(r'^signup/$', views.signup, name='signup'),
]
