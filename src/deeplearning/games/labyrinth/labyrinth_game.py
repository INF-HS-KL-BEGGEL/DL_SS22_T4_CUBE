import copy
import random
from deeplearning.games.game import Game
from deeplearning.games.labyrinth.labyrinth import Labyrinth, TileType


class LabyrinthGame(Game):

    def __init__(self, labyrinth):
        super().__init__()
        self.labyrinth = labyrinth
        self.start_tile = self.get_start_tile()
        self.current_tile = self.start_tile
        self.maze_copy = copy.deepcopy(self.labyrinth)

    @staticmethod
    def setup_game(heigth = 10, width = 10, target_count = 4, seed = 0):
        """Factory Method"""
        maze = Labyrinth.generate_maze(heigth, width, seed)
        LabyrinthGame.create_random_targets(maze, target_count)
        return LabyrinthGame(maze)

    @staticmethod
    def create_random_targets(maze, target_count):
        """Maze ist InOut Param"""

        if target_count > len(maze.get_all_accessible_tiles()):
            raise Exception("Not enough accessible tiles")
        if target_count > 0:
            random_tiles_index = random.sample(range(1, len(maze.get_all_accessible_tiles()) - 1), target_count - 1)

            for index in random_tiles_index:
                tile = maze.get_all_accessible_tiles()[index]
                maze.set_target(tile)

    def get_current_tile(self):
        return self.current_tile

    def get_start_tile(self):
        for tile in self.labyrinth.get_all_accessible_tiles():
            if tile.get_type() == TileType.START:
                return tile
        raise Exception("No start tile found")

    def get_tiles(self):
        return self.labyrinth.get_tiles()

    def get_targets(self):
        return self.labyrinth.get_targets()

    def get_current_target(self):
        return self.get_targets()[-1]

    def get_current_targets(self):
        return self.get_targets()

    def get_labyrinth(self):
        return self.labyrinth

    def check_current_for_target(self):
        tile = self.get_current_tile()
        if tile.get_type() == TileType.TARGET:
            return True
        return False

    def collect_target(self):
        self.get_current_tile().tile_type = TileType.EMPTY

    def is_accessible(self, direction):
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        return self.labyrinth.is_accessible_tile(tile)

    def reset_game(self):
        # maze = Labyrinth.create_from("./games/labyrinth/test_labyrinth.json")
        self.start_tile = self.get_start_tile()
        self.current_tile = self.start_tile
        self.labyrinth = copy.deepcopy(self.maze_copy)

    def is_done(self):
        return len(self.labyrinth.get_targets()) == 0

    def go(self, direction):
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        if not tile or tile.get_type() == TileType.BLOCKED:
            return TileType.BLOCKED

        self.current_tile = tile
        if self.check_current_for_target():
            self.collect_target()
            return TileType.TARGET
        return TileType.EMPTY
