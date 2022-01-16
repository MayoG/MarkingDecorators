from dec import class_functions_dictionary, MetaMark


class Bakery(metaclass=MetaMark):
    cooking_styles = class_functions_dictionary()

    @cooking_styles("indian")
    def indian_backing(self):
        pass

    @cooking_styles("asian")
    def asian_backing(self):
        pass

    @cooking_styles("asian")
    def asian_spicy_backing(self):
        pass

    @classmethod
    def get_cooking_styles(cls):
        """Get the events of the routine
        Returns:
            dict[str, list[Callback]]: The events callbacks mapped by their events
        """

        return cls.cooking_styles.all(cls)
