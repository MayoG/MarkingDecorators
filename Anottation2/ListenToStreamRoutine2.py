from Routine2 import Routine


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


if __name__ == '__main__':
    print(f"events: {ListenToStream.events.all}")
    print(ListenToStream.events.all["Phase1"])

    # l = ListenToStream()
    # print(f"events: {l.get_events()}")
    # l.pace("dsada")
    # print(f"events: {l.get_events()}")
    # print(f"food: {l.get_food()}")
