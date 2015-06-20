from time import gmtime, strftime

class Cell:
    NORTH_WALL = 'N'
    SOUTH_WALL = 'S'
    WEST_WALL = 'W'
    EAST_WALL = 'E'

    def __init__(self, x, y):
        self.__x = x
        self.__y = y
        self.__visited = False
        self.__walls = {
            'N': 0,
            'S': 0,
            'E': 0,
            'W': 0
        }

    def markVisited(self):
        self.__visited = True

    def visited(self):
        return self.__visited
    
    def getX(self):
        return self.__x
    
    def getY(self):
        return self.__y

    def getWallsRaw(self):
        return str(self.__walls)

    def getWallsDict(self):
        return self.__walls

    def setWallsDict(self, walls):
        self.__walls = walls

    def hasWall(self, direction):
        return False if direction in self.__walls.keys() and self.__walls[direction] == 1 else True

    def clearWall(self, wall):
        if wall not in self.__walls.keys():
            print '[%s - Error]: Invalid wall provided' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            raise Exception("Invalid wall provided")

        self.__walls[wall] = 1