def _make_registrar():
    registry = {}
    def registrar(func):
        registry[func.__name__] = func
        return func  # normally a decorator returns a wrapped function, 
                        # but here we return func unmodified, after registering it
    registrar.all = registry
    return registrar



class Routine():
    extensions = _make_registrar()
    food = _make_registrar()
    def __init__(self):
        pass
    
    def get_extensions(self):
        return self.extensions.all
    
    def get_food(self):
        return self.food.all

# print(r.get_methods())