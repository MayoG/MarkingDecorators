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
    # {'asian': {<function Bakery.asian_spicy_backing at 0x014AA340>,
    #           <function C.asian_in_c at 0x014AA3D0>,
    #           <function D.asian1 at 0x014AA460>,
    #           <function Bakery.asian_backing at 0x014AA2F8>},
    # 'indian': {<function Bakery.indian_backing at 0x014AA2B0>}}

    print(f"{C.get_cooking_styles() = }")  # Expecting to get the same only without D cooking styles (asian1 method).
    # {'asian': {<function Bakery.asian_spicy_backing at 0x014AA340>,
    #           <function C.asian_in_c at 0x014AA3D0>,
    #           <function Bakery.asian_backing at 0x014AA2F8>},
    # 'indian': {<function Bakery.indian_backing at 0x014AA2B0>}}
