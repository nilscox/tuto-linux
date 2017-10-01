def chanmsg(bot, args):
    to = args[0]
    msg = " ".join(args[1:])
    bot.send_message(to, msg)
    return "Message send."
