from constants import DEBUG

handlers = {}


def subscribe(event, func):
    if handlers.get(event) is None:
        handlers[event] = []
    handlers[event].append(func)


def publish(event, *args, **kwargs):
    if DEBUG:
        print(event, '[' + ', '.join(map(str, args)) + ']', kwargs)

    if handlers.get(event) is None:
        return

    for func in handlers[event]:
        func(*args, **kwargs)
