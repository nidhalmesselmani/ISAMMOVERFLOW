from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from channels.generic.websockets import WebsocketDemultiplexer
from channels.binding.websockets import WebsocketBinding

# Create your models here.



class Feed(models.Model):
    user = models.ForeignKey(User)
    date = models.DateTimeField(auto_now_add=True)
    post = models.TextField(max_length=255)
    likes = models.IntegerField(default=0)
    comments = models.IntegerField(default=0)

    def __str__(self):
        return self.post


class FeedBinding(WebsocketBinding):

    model = Feed
    stream = "intval"
    fields = ["user", "date","post","likes","comments"]
    


    @classmethod
    def group_names(cls, instance):
        return ["intval-updates"]

    def has_permission(self, user, action, pk):
        return True


def create_user_feed(sender, instance, created, **kwargs):
    if created:
        Feed.objects.create(
            user=instance, post="{0} has joined the network".format(instance))


post_save.connect(create_user_feed, sender=User)

class Demultiplexer(WebsocketDemultiplexer):

    consumers = {
        "intval": FeedBinding.consumer,
    }

    def connection_groups(self):
        return ["intval-updates"]
