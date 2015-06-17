class Generator:
    def __init__(self, strategy):
        self.__strategy = strategy

    def generate(self):
        if 'generate' not in dir(self.__strategy):
            raise NotImplementedError

        self.__strategy.generate()

    def getRaw(self):
        if 'getRaw' not in dir(self.__strategy):
            raise NotImplementedError

        return self.__strategy.getRaw()

    def getJSON(self):
        if 'getJSON' not in dir(self.__strategy):
            raise NotImplementedError

        return self.__strategy.getJSON()

    def __repr__(self):
        return self.__strategy.__repr__()

    def __str__(self):
        return self.__strategy.__str__()
