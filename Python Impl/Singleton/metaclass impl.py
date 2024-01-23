from threading import Lock, Thread

"""Meta class that will define the behaviour of all the subclasses"""
class SingletonMeta(type):
    _instances = {}
    _lock: Lock = Lock()

    """ if below call is not overriden singleton pattern will not be followed """

    def __call__(cls, *args, **kwargs):
        if cls not in cls._instances:
            with cls._lock:
                instance = super().__call__(*args, **kwargs)
                cls._instances[cls] = instance
        return cls._instances[cls]


class Singleton(metaclass=SingletonMeta):
    value: str = None

    def __init__(self, value: str) -> None:
        self.value = value

    def some_operation(self):
        return self.value + self.value


def test_singleton(value: str) -> None:
    singleton = Singleton(value)
    print(singleton.value)


if __name__ == '__main__':
    process1 = Thread(target=test_singleton("BAR"))
    process2 = Thread(target=test_singleton("FOO"))
    process1.start()
    process2.start()
