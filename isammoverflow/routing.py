# In routing.py
from channels.routing import route,route_class
from feeds.consumers import ws_message, ws_add, ws_disconnect
from feeds.models import FeedBinding,Demultiplexer

channel_routing = [
    route("websocket.connect", ws_add),
    route("websocket.receive", ws_message),
    route("websocket.disconnect", ws_disconnect),
    route_class(Demultiplexer, path="^/feeds/"),

]
