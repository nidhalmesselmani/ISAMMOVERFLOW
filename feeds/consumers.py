from channels import Group
# Connected to websocket.receive


def ws_message(message):
    Group("chat").send({
        "text": "[user] %s" % message.content['text'],
    })


# Connected to websocket.connect
def ws_add(message):
    # Accept the incoming connection
    message.reply_channel.send({"accept": True})
    # Add them to the chat group
    Group("chat").add(message.reply_channel)


# Connected to websocket.disconnect
def ws_disconnect(message):
    Group("chat").discard(message.reply_channel)
