from collections import defaultdict
import re
from functools import partial


def _make_registrar2():
    registry = defaultdict(lambda: defaultdict(set))

    def key_registrar(key):
        if callable(key):
            return registrar(key="default_key", function=key)
        else:
            return partial(registrar, key=key)

    def registrar(function, key):
        class_name = re.search(' (.*)\\.', function.__str__()).group(1)
        registry[class_name][key].add(function)
        return registrar

    key_registrar.all = registry

    return key_registrar


class Routine:
    events = _make_registrar2()

    def __init__(self):
        pass

    @events("Aba")
    def start(self):
        pass

    @classmethod
    def get_events(cls):
        routine_events = cls.events.all[Routine.__name__]
        for event_name, events_functions in routine_events.items():
            cls.events.all[cls.__name__][event_name].update(events_functions)
        return cls.events.all[cls.__name__]


class ListenToStream(Routine):
    def __init__(self):
        super().__init__()

    @Routine.events("Phase1")
    def pace(self, a):
        print(a)

    @Routine.events("Phase1")
    def cake(self, a, b):
        pass

    @Routine.events
    def banana(self):
        pass


class ListenToStream2(Routine):
    def __init__(self):
        super().__init__()

    @Routine.events("Aba")
    def pace1(self, a):
        print(a)

    @Routine.events("Aba")
    def cake1(self, a, b):
        pass

    @Routine.events
    def banana1(self):
        pass


if __name__ == '__main__':
    print(ListenToStream.get_events())
    # defaultdict(<class 'set'>, {'Phase1': {<function ListenToStream.pace at 0x7f2c9cfdfdc0>,
    #                                        <function ListenToStream.cake at 0x7f2c9cfdfe50>},
    #                             'default_key': {<function ListenToStream.banana at 0x7f2c9cfdfee0>},
    #                             'Aba': {<function Routine.start at 0x7f2c9cfdfc10>}})
    print(ListenToStream2.get_events())
    # defaultdict(<class 'set'>, {'Aba': {<function Routine.start at 0x7f2c9cfdfc10>,
    #                                     <function ListenToStream2.pace1 at 0x7f2c9cfe3040>,
    #                                     <function ListenToStream2.cake1 at 0x7f2c9cfe30d0>},
    #                             'default_key': {<function ListenToStream2.banana1 at 0x7f2c9cfe3160>}})
