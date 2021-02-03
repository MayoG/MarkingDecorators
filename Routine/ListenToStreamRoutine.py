from Routine import Routine

class ListenToStream(Routine):
    def __init__(self, a):
        super().__init__()
        self.a = a

    @Routine.extensions
    def pace(self, a):
        pass

    @Routine.food
    def cake(self):
        print(self.a)

    @Routine.extensions
    @Routine.food
    def banana(self):
        pass


l = ListenToStream(1)
l2 = ListenToStream(4)
print(f"extensions: {l.get_extensions()}")
print(f"food: {l.get_food()}")

l.get_food()["cake"](l)
l2.get_food()["cake"](l2)
