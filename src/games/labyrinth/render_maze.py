from tkinter import *
from games.labyrinth.labyrinth import Labyrinth, TileType


class LabyrinthRenderer:
    def __init__(self, labyrinth: Labyrinth, current_tile):
        self.maze_map = labyrinth.get_maze_map()

        self.master = Tk()
        self.master.title("QLearning Maze")

        self.pixel_size = 25

        canvas_width = len(self.maze_map[0]) * self.pixel_size
        canvas_height = len(self.maze_map) * self.pixel_size
        self.canvas = Canvas(self.master,
                             width=canvas_width,
                             height=canvas_height)
        self.canvas.pack()
        self.draw_maze(self.maze_map, current_tile)

    def draw_maze(self, maze_map, current_tile):
        current_y = 0
        for i in maze_map:
            current_x = 0
            for j in i:
                color = LabyrinthRenderer.get_tile_color(j)
                self.canvas.create_rectangle(current_x, current_y, current_x + self.pixel_size, current_y + self.pixel_size, fill=color)
                current_x += self.pixel_size
            current_y += self.pixel_size

        # draw the current tile when the maze map is drawn
        self.canvas.create_rectangle(current_tile.y * self.pixel_size, current_tile.x *  self.pixel_size, current_tile.y * self.pixel_size + self.pixel_size,
                                     current_tile.x * self.pixel_size + self.pixel_size, fill='#03adfc')

    @staticmethod
    def get_tile_color(tile):
        color_start = "#a134eb"
        color_empty = "#ffffff"
        color_blocked = "#000000"
        color_target = "#03fc7b"

        if tile.tile_type is TileType.TARGET:
            return color_target
        elif tile.tile_type is TileType.EMPTY:
            return color_empty
        elif tile.tile_type is TileType.BLOCKED:
            return color_blocked
        elif tile.tile_type is TileType.START:
            return color_start
