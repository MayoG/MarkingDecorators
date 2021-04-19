from collections import defaultdict


def _make_registrar():
    registry = defaultdict(list)

    def registrar(params_or_func):
        if callable(params_or_func):
            if (not hasattr(registrar, "last_params")) or (registrar.last_params is None):
                registrar.last_params = "default_key"
            registry[registrar.last_params].append(params_or_func)
            registrar.last_params = None
            return params_or_func
        else:
            registrar.last_params = params_or_func
            return registrar

    registrar.all = registry
    return registrar


class Routine:
    events = _make_registrar()

    def __init__(self):
        pass

    def get_events(self):
        return self.events.all
