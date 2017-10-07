handlers = {}


def subscribe(event, func):
    if handlers.get(event) is None:
        handlers[event] = []
    handlers[event].append(func)


def trigger(event, *args, **kwargs):
    if handlers.get(event) is None:
        return

    for func in handlers[event]:
        func(*args, **kwargs)
