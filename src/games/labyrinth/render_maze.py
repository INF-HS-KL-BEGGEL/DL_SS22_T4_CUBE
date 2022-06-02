from tkinter import *

from games.labyrinth.labyrinth import Labyrinth, TileType

maze_size = 15
maze = Labyrinth.generate_maze(maze_size, maze_size).maze_map

print(maze)
canvas_width = maze_size * 50
canvas_height = maze_size * 50

color_start = "#0F0"
color_empty = "#EEE"
color_blocked = "#000"
color_target = "#FF0"

master = Tk()

w = Canvas(master,
           width=canvas_width,
           height=canvas_height)
w.pack()

x = 0
y = 0
color = color_empty

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
        w.create_rectangle(x, y, x + 50, y + 50, fill=color)
        x += 50
    y += 50

mainloop()
