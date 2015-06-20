class Solver:
    def __init__(self, strategy):
        self.__strategy = strategy

    def solve(self):
        if 'solve' not in dir(self.__strategy):
            raise NotImplementedError

        self.__strategy.solve()

    def getRawPath(self):
        if 'getRawPath' not in dir(self.__strategy):
            raise NotImplementedError

        return self.__strategy.getRawPath()

    def getJSONPath(self):
        if 'getJSONPath' not in dir(self.__strategy):
            raise NotImplementedError

        return self.__strategy.getJSONPath()

    def __repr__(self):
        return self.__strategy.__repr__()

    def __str__(self):
        return self.__strategy.__str__()
