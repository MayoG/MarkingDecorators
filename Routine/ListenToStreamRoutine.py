from Routine import Routine


class ListenToStream(Routine):
    def __init__(self):
        super().__init__()

    @Routine.extensions
    def pace(self, a):
        pass

    @Routine.food
    def cake(self, a, b):
        pass

    @Routine.extensions
    @Routine.food
    def banana(self):
        pass


l = ListenToStream()
print(f"extensions: {l.get_extensions()}")
print(f"food: {l.get_food()}")
