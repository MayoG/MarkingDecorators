from bakery_example.bakery import Bakery


class C(Bakery):
    def __init__(self) -> None:
        super().__init__()

    @Bakery.cooking_styles("asian")
    def asian_in_c(self):
        pass


class D(C):
    def __init__(self) -> None:
        super().__init__()

    @C.cooking_styles("asian")
    def asian1(self):
        pass


if __name__ == '__main__':
    print(f"{D.get_cooking_styles() = }")
    print(f"{C.get_cooking_styles() = }")
