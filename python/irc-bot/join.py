def join(bot, args):

    channel = args[0]
    key = ""
    if len(args) > 1:
        key = args[1]

    bot.join_channel(channel, key)

    return "You're connect to " + str(channel)
