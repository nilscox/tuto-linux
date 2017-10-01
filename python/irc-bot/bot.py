import irc.client


class Bot(irc.client.SimpleIRCClient):
    def __init__(self, functable):
        irc.client.SimpleIRCClient.__init__(self)
        self.functable = functable

    def on_welcome(self, connection, event):
        print('Welcome!')

    def on_join(self, connection, event):
        print('join:' + event.target)

    def on_privmsg(self, connection, event):
        print('privmsg' + str(event))

        sender = event.source.split("!")[0]
        splitted = event.arguments[0].split(" ")
        command = splitted[0]
        args = splitted[1:]

        for function in self.functable:
            if function.__name__ == command:
                result = function(self, args)
                if result:
                    self.send_message(sender, result)

    def send_message(self, to, msg):
        self.connection.privmsg(to, msg)

    def join_channel(self, channel, key=''):
        self.connection.join(channel, key)
