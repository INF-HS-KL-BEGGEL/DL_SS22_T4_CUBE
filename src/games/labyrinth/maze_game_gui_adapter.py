import time

from games.labyrinth.labyrinth import Direction, Labyrinth, Tile, TileType
from games.game import Game
from games.labyrinth.actions import GoAction
import copy
import random
from games.labyrinth.labyrinth_game import LabyrinthGame
from games.labyrinth.render_maze import LabyrinthRenderer


class LabyrinthGameGuiAdapter(Game):

    def __init__(self, maze_game: LabyrinthGame):
        super().__init__()
        self.maze_game = maze_game
        self.labyrinth_renderer = LabyrinthRenderer(self.maze_game.get_labyrinth(), self.maze_game.get_current_tile())

    def create_targets(self, maze, target_count):
        self.maze_game.create_targets(maze, target_count)

    def get_current_tile(self):
        return self.maze_game.get_current_tile()

    def get_start_tile(self):
        return self.maze_game.get_start_tile()

    def get_tiles(self):
        return self.maze_game.get_tiles()

    def get_targets(self):
        return self.maze_game.get_targets()

    def get_current_target(self):
        return self.maze_game.get_current_target()

    def get_current_targets(self):
        return self.maze_game.get_current_targets()

    def get_labyrinth(self):
        return self.maze_game.get_labyrinth()

    def check_current_for_target(self):
        return self.maze_game.check_current_for_target()

    def collect_target(self):
        self.maze_game.collect_target()

    def is_accessible(self, direction):
        return self.maze_game.is_accessible(direction)

    def reset_game(self):
        self.labyrinth_renderer.draw_maze(self.maze_game.get_labyrinth().get_maze_map())
        return self.maze_game.reset_game()

    def is_done(self):
        return self.maze_game.is_done()

    def go(self, direction):
        self.labyrinth_renderer.draw_current_tile(self.maze_game.get_current_tile())
        return self.maze_game.go(direction)