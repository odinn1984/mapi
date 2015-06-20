from Maze import Maze
from IMazeGenerator import IMazeGenerator

class Strategy_RecursiveBacktracker(IMazeGenerator):
    def __init__(self, width, height):
        self.__maze = Maze(width, height)

    def generate(self):
        cell_stack = list()
        current_cell = self.__maze.getRandomOrigin()
        self.__maze.markVisitedCell(current_cell)

        while self.__maze.hasUnvisitedCells() == True:
            if self.__maze.hasUnvisitedNeightbours(current_cell) == True:
                unvisited_cell = self.__maze.getRandomUnvisitedNeightbour(current_cell)
                cell_stack.append(current_cell)
                self.__maze.removeWallBettweCells(current_cell, unvisited_cell)
                current_cell = unvisited_cell
                self.__maze.markVisitedCell(current_cell)
            elif len(cell_stack) > 0:
                current_cell = cell_stack.pop()
            else:
                current_cell = self.__maze.getRandomUnvisitedCellr()
                self.__maze.markVisitedCell(current_cell)

        self.__maze.addEntryAndExitPoints()

    def getRaw(self):
        return self.__maze.getRaw()

    def getJSON(self):
        return self.__maze.getJSON()

    def __str__(self):
        return 'Strategy_RecursiveBacktracker'


