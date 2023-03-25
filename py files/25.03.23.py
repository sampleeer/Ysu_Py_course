class CrazyMonkeyPack(type):

    def __new__(mcs, name, bases, dict):
        cls = type.__new__(mcs, name, bases, dict)

        def wrapper(*args):
            instance = []
            for i in range(1, args[0]+1):
                monkey = cls(f'monkey #{i}')  # calls __init__
                monkey.state = 'crazy'  # monkey-patches the state attribute
                instance.append(monkey)
            return instance

        return wrapper


class CrazyMonkeys(metaclass=CrazyMonkeyPack):
    """A self-expanding horde of monkeys"""
    def __init__(self, name):
        self.name = name

    def __repr__(self):
        return f"<{self.name} ({self.state})>"


monkeys = CrazyMonkeys(3)  # calls __new__
print(monkeys)             # see what happens!
