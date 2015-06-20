import random
import json

class Player:
    def __init__(self, maze):
        self.__path = []
        self.__current_cell = maze.getOriginOfMaze()
        self.__end_cell = maze.getEndOfMaze()
        self.__maze = maze
        self.__current_direction = None
        self.__directions = {
            'N': (0, -1),
            'S': (0, 1),
            'E': (-1, 0),
            'W': (1, 0)
        }

    def chooseRandomDirection(self):
        self.__current_direction = random.sample(
            self.__directions if not self.isPlayerAtOrigin() else dict((k, self.__directions[k]) for k in ['E', 'W', 'S']),
        1)[0]

    def moveInCurrentDirectionUntilHitWall(self):
        while not self.__current_cell.hasWall(self.__current_direction) and not self.reachedEndOfMaze():
            self.addCurrentCellToPath()

            self.__current_cell = self.__maze.getCellAt(
                self.__current_cell.getX() + self.__directions[self.__current_direction][0],
                self.__current_cell.getY() + self.__directions[self.__current_direction][1]
            )

        if self.reachedEndOfMaze():
            self.addCurrentCellToPath()

    def addCurrentCellToPath(self):
        self.__path.append({
            'x': self.__current_cell.getX(),
            'y': self.__current_cell.getY()
        })

    def isPlayerAtOrigin(self):
        return True if \
            self.__current_cell.getX() == self.__maze.getOriginOfMaze().getX() and \
            self.__current_cell.getY() == self.__maze.getOriginOfMaze().getY() else False

    def reachedEndOfMaze(self):
        return True if \
            self.__current_cell.getX() == self.__end_cell.getX() and \
            self.__current_cell.getY() == self.__end_cell.getY() else False

    def getRawPath(self):
        return str(self.__path)

    def getJSONPath(self):
        print self.__path
        return json.dumps(self.__path)
