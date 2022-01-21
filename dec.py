from collections import defaultdict
from functools import partial
from inspect import isclass

# Future update can be removed if we change the decorator from function to class and check the type of the attribute
# instead of checking if it has this signature as attribute
MY_CLASS_SIGNATURE = "MY_CLASS_SIGNATURE"


class MetaMark(type):
    def __new__(mcs, name, bases, dct):
        x = super().__new__(mcs, name, bases, dct)

        for class_attribute in dct.values():
            if hasattr(class_attribute, MY_CLASS_SIGNATURE):
                mcs.fix_registry(class_attribute, x, name)
        for base_class in bases:
            for class_attribute_name in dir(base_class):
                if hasattr(getattr(base_class, class_attribute_name), MY_CLASS_SIGNATURE):
                    mcs.fix_registry(getattr(base_class, class_attribute_name), x, name)
        return x

    @staticmethod
    def fix_registry(key_registrar, update_class, class_name):
        key_registrar.registry[update_class] = key_registrar.registry[class_name]
        del key_registrar.registry[class_name]

    @staticmethod
    def create_functions_dictionary():
        """Create a decorator for marking functions and storing them in a
            dictionary by their class and their marking signature
            Returns:
                Decorator that stores its functions in the 'all' attribute.
            Example usage:
            >>> class Bakery(metaclass=MetaMark):
            ...     cooking_styles = MetaMark.create_functions_dictionary()
            ...
            ...     @cooking_styles("indian")
            ...     def indian_backing(self):
            ...         pass
            ...
            ...     @cooking_styles("asian")
            ...     def asian_backing(self):
            ...         pass
            ...
            ...     @classmethod
            ...     def get_cooking_styles(cls):
            ...         return cls.cooking_styles.all(cls)

            >>> print(Bakery.get_cooking_styles()) # {'indian': {<function Bakery.indian_backing at 0x03B68100>},
            ...                                    #  'asian': {<function Bakery.asian_backing at 0x03B68148>}}
            """

        registry = defaultdict(lambda: defaultdict(set))

        def key_registrar(keys_or_function):
            if callable(keys_or_function):
                # No key was given to the function, setting a defualt key
                return register(keys="default_key", function=keys_or_function)
            else:
                return partial(register, keys=keys_or_function)

        def register(function, keys):
            function_class_name = function.__qualname__.split(".")[0]

            keys = [keys] if not isinstance(keys, list) else keys

            for key in keys:
                registry[function_class_name][key].add(function)

            return function

        def get_functions(class_or_object):
            cls = class_or_object if isclass(class_or_object) else type(class_or_object)

            for class_object in registry:
                if issubclass(cls, class_object):
                    for function_key, functions in registry[class_object].items():
                        registry[cls][function_key].update(functions)

            return registry[cls]

        key_registrar.all = get_functions
        key_registrar.registry = registry

        key_registrar.MY_CLASS_SIGNATURE = MY_CLASS_SIGNATURE

        return key_registrar
