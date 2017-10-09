
from django.conf.urls import url
from .views import IndexView,FeedsList

urlpatterns = [
   url(r'^$',FeedsList.as_view()),
 
]
