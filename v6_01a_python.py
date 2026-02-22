class SafeStorage:
    def __init__(self):
        self.__data = None

    def get(self):
        return self.__data

    def put(self, data):
        self.__data = data
