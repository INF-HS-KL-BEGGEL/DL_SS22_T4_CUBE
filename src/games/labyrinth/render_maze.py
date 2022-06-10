from tkinter import *
from games.labyrinth.labyrinth import Labyrinth, TileType

class LabyrinthRenderer:

    def __init__(self, labyrinth: Labyrinth, current_tile):
        self.color_mapping = {
            TileType.START: "#a134eb",
            TileType.EMPTY: "#ffffff",
            TileType.BLOCKED: "#000000",
            TileType.TARGET: "#03fc7b"
        }


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
        self.draw_maze(self.maze_map)
        # draw the current tile when the maze map is drawn
        self.previous_tile = current_tile
        self.draw_current_tile(current_tile)

    def draw_maze(self, maze_map):
        current_y = 0
        for i in maze_map:
            current_x = 0
            for j in i:
                color = self.get_tile_color(j)
                self.canvas.create_rectangle(current_x, current_y,
                                             current_x + self.pixel_size,
                                             current_y + self.pixel_size, fill=color)
                current_x += self.pixel_size
            current_y += self.pixel_size

    def draw_current_tile(self, current_tile):
        color = self.get_tile_color(self.previous_tile)
        # reset the previous tile
        self.canvas.create_rectangle(self.previous_tile.y * self.pixel_size, self.previous_tile.x * self.pixel_size,
                                     self.previous_tile.y * self.pixel_size + self.pixel_size,
                                     self.previous_tile.x * self.pixel_size + self.pixel_size, fill=color)
        # draw the current tile
        self.canvas.create_rectangle(current_tile.y * self.pixel_size, current_tile.x * self.pixel_size,
                                     current_tile.y * self.pixel_size + self.pixel_size,
                                     current_tile.x * self.pixel_size + self.pixel_size, fill='#03adfc')

        # update the previous tile for the next iteration
        self.previous_tile = current_tile
        self.master.update()

    def get_tile_color(self, tile):
        return self.color_mapping[tile.get_type()]
