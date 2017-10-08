handlers = {}


def subscribe(event, func):
    if handlers.get(event) is None:
        handlers[event] = []
    handlers[event].append(func)


def publish(event, *args, **kwargs):
    print(event)

    if handlers.get(event) is None:
        return

    for func in handlers[event]:
        func(*args, **kwargs)
