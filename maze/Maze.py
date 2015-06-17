import itertools
import random
import json

from Cell import Cell
from time import gmtime, strftime

class Maze:
    def __init__(self, width, height):
        self.__unvisited_cell_count = width * height
        self.__maze = [[Cell(x, y) for x in range(0, width)] for y in range(0, height)]
        self.__unvisited_cells = list(itertools.product([x for x in range(0, width)], [y for y in range(0, height)]))
        self.__width = width
        self.__height = height

    def getOrigin(self):
        return self.__maze[random.randint(0, self.__height - 1)][random.randint(0, self.__width - 1)]

    def hasUnvisitedCells(self):
        return True if self.__unvisited_cell_count > 0 else False

    def hasUnvisitedNeightbours(self, cell):
        x = cell.getX()
        y = cell.getY()

        if x - 1 >= 0 and self.__maze[y][x - 1].visited() == False:
            return True
        if y - 1 >= 0 and self.__maze[y - 1][x].visited() == False:
            return True
        if x + 1 < self.__width and self.__maze[y][x + 1].visited() == False:
            return True
        if y + 1 < self.__height and self.__maze[y + 1][x].visited() == False:
            return True

        return False

    def getRandomUnvisitedCellr(self):
        unvisited_cells = self.__unvisited_cells
        random.shuffle(unvisited_cells)
        unvisited_cell = unvisited_cells[0]
        self.__unvisited_cells.remove(unvisited_cell)

        return self.__maze[unvisited_cell[1]][unvisited_cell[0]]

    def getRandomUnvisitedNeightbour(self, cell):
        x = cell.getX()
        y = cell.getY()
        neightbours = [
            (x - 1, y),
            (x + 1, y),
            (x, y - 1),
            (x, y + 1)
        ]
        random.shuffle(neightbours)
        selected_neightbour = None

        for neightbour in neightbours:
            if neightbour[0] < 0 or neightbour[0] >= self.__width or neightbour[1] >= self.__height or neightbour[1] < 0:
                continue

            if self.__maze[neightbour[1]][neightbour[0]].visited() == True:
                continue

            selected_neightbour = self.__maze[neightbour[1]][neightbour[0]]

        return selected_neightbour

    def markVisitedCell(self, cell):
        x = cell.getX()
        y = cell.getY()

        self.__maze[y][x].markVisited()
        self.__unvisited_cells.remove((x, y))
        self.__unvisited_cell_count = self.__unvisited_cell_count - 1

    def removeWallBettweCells(self, cella, cellb):
        x_a = cella.getX()
        x_b = cellb.getX()
        y_a = cella.getY()
        y_b = cellb.getY()
        diff_x = x_a - x_b
        diff_y = y_a - y_b

        if x_a == x_b:
            if diff_y < 0:
                self.__maze[y_a][x_a].clearWall(Cell.SOUTH_WALL)
                self.__maze[y_b][x_b].clearWall(Cell.NORTH_WALL)
            else:
                self.__maze[y_a][x_a].clearWall(Cell.NORTH_WALL)
                self.__maze[y_b][x_b].clearWall(Cell.SOUTH_WALL)
        elif y_a == y_b:
            if diff_x < 0:
                self.__maze[y_a][x_a].clearWall(Cell.WEST_WALL)
                self.__maze[y_b][x_b].clearWall(Cell.EAST_WALL)
            else:
                self.__maze[y_a][x_a].clearWall(Cell.EAST_WALL)
                self.__maze[y_b][x_b].clearWall(Cell.WEST_WALL)
        else:
            print '[%s - Error]: Invalid cell pair provided' % (strftime("%Y-%m-%d %H:%M:%S", gmtime()))
            raise Exception("Invalid cell pair provided")

    def getRaw(self):
        final_result = ""

        for cell_row in self.__maze:
            row_list = []

            for cur_cell in cell_row:
                row_list.append(cur_cell.getWallsRaw())

            final_result = final_result + '[' + ','.join(row_list) + ']\r\n'

        return final_result

    def getJSON(self):
        final_result = []

        for cell_row in self.__maze:
            row_list = []

            for cur_cell in cell_row:
                row_list.append(cur_cell.getWallsDict())

            final_result.append(row_list)

        return json.dumps(final_result)