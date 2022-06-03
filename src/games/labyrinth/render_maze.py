from tkinter import *
from games.labyrinth.labyrinth import Labyrinth, TileType


def setup_window(size):
    canvas_width = size * 50
    canvas_height = size * 50

    master = Tk()
    master.title("QLearning Maze")

    w = Canvas(master,
               width=canvas_width,
               height=canvas_height)
    w.pack()

    return w


def render_maze(canvas: Canvas, labyrinth: Labyrinth):
    maze = labyrinth.get_maze_map()

    color_start = "#0F0"
    color_empty = "#EEE"
    color_blocked = "#000"
    color_target = "#FF0"
    color = color_empty

    y = 0
    for i in maze:
        x = 0
        for j in i:
            print(j)
            if j.tile_type is TileType.TARGET:
                color = color_target
            elif j.tile_type is TileType.EMPTY:
                color = color_empty
            elif j.tile_type is TileType.BLOCKED:
                color = color_blocked
            elif j.tile_type is TileType.START:
                color = color_start
            canvas.create_rectangle(x, y, x + 50, y + 50, fill=color)
            x += 50
        y += 50


maze_size = 20
c = setup_window(maze_size)
render_maze(c, Labyrinth.generate_maze(maze_size, maze_size))
mainloop()
