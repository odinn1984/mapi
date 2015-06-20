from Player import Player
from IMazeSolver import IMazeSolver

class Strategy_RandomMouse(IMazeSolver):
    def __init__(self, maze):
        self.__maze = maze
        self.__player = Player(maze)

    def solve(self):
        while not self.__player.reachedEndOfMaze():
            self.__player.chooseRandomDirection()
            self.__player.moveInCurrentDirectionUntilHitWall()

        print "Done!"

    def getRawPath(self):
        return self.__player.getRawPath()

    def getJSONPath(self):
        return self.__player.getJSONPath()

    def __str__(self):
        return 'Strategy_RandomMouse'


