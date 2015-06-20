from Maze import Maze
from IMazeGenerator import IMazeGenerator

class Strategy_HuntAndKill(IMazeGenerator):
    def __init__(self, width, height):
        self.__maze = Maze(width, height)

    def generate(self):
        current_cell = self.__maze.getRandomOrigin()
        self.__maze.markVisitedCell(current_cell)
        have_more_cells_to_hunt = True

        while have_more_cells_to_hunt:
            while self.__maze.hasUnvisitedNeightbours(current_cell) == True:
                unvisited_cell = self.__maze.getRandomUnvisitedNeightbour(current_cell)
                self.__maze.removeWallBettweCells(current_cell, unvisited_cell)
                current_cell = unvisited_cell
                self.__maze.markVisitedCell(current_cell)

            current_cell = self.huntForAvailableCell()

            if current_cell is None:
                have_more_cells_to_hunt = False

    def huntForAvailableCell(self):
        for cell in self.__maze.cells():
            if self.__maze.hasUnvisitedNeightbours(cell):
                print (cell.getX(), cell.getY())
                return cell

        return None


    def getRaw(self):
        return self.__maze.getRaw()

    def getJSON(self):
        return self.__maze.getJSON()

    def __str__(self):
        return 'Strategy_HuntAndKill'


