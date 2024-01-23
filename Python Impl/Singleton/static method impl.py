from threading import Lock

class Singleton:
    _instance = None
    _lock = Lock()

    @staticmethod
    def get_instance(value):
        with Singleton._lock:
            if Singleton._instance is None:
                Singleton._instance = Singleton(value)
        return Singleton._instance

    def __init__(self, value):
        if Singleton._instance is not None:
            raise Exception("Singleton instance already exists. Use get_instance() method.")
        self.value = value

    def some_operation(self):
        return self.value + self.value

if __name__ == '__main__':
    instance1 = Singleton.get_instance("FOO")
    # Output: FOOFOO
    print(instance1.some_operation())
    instance2 = Singleton.get_instance("BAR")
    # Output: FOOFOO
    print(instance2.some_operation())
