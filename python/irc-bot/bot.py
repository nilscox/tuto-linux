import irc.client

class Bot(irc.client.SimpleIRCClient):

    def __init__(self, clazz):
        irc.client.SimpleIRCClient.__init__(self)
        self.handlers = []
        for c in clazz:
            self.handlers.append(c())

    def on_welcome(self, connection, event):
        print('Welcome!')

    def on_privmsg(self, connection, event):
        print('privmsg' + str(event))

        sender = event.source.split("!")[0]
        splitted = event.arguments[0].split(" ")
        command = splitted[0].lower()
        args = splitted[1:]

        for handler in self.handlers:
            if type(handler).__name__.lower() == command:
                result = handler.command(args)
                if result:
                    self.send_message(sender, result)

    def send_message(self, to, msg):
        self.connection.privmsg(to, msg)

