from games.labyrinth.labyrinth import Direction, Labyrinth, Tile, TileType
from games.game import Game
from games.labyrinth.actions import GoAction
import copy


class LabyrinthGame(Game):

    def __init__(self, labyrinth):
        super().__init__()
        self.labyrinth = labyrinth
        self.current_tile = self.labyrinth.get_start_tile()
        self.start_tile = self.labyrinth.get_start_tile()
        self.targets = self.labyrinth.get_all_target_tiles()

        # copy for reset_game
        self.start_tile_copy = copy.deepcopy(self.start_tile)
        self.targets_copy = copy.deepcopy(self.targets)

    def get_current_tile(self):
        return self.current_tile

    def get_tiles(self):
        return self.labyrinth.get_tiles()

    def get_targets(self):
        return self.targets

    def get_labyrinth(self):
        return self.labyrinth

    def get_current_target(self):
        if not self.is_done():
            return self.targets[0]

    def check_for_target(self):
        tile = self.get_current_tile()
        if tile.get_type() == TileType.TARGET:
            self.targets.pop(0)
            return True
        return False

    @staticmethod
    def setup_game():
        """Factory Method"""
        maze = Labyrinth.create_from("./games/labyrinth/test_labyrinth.json")
        return LabyrinthGame(maze)

    def is_accessible(self, direction):
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        return self.labyrinth.is_accessible_tile(tile)

    def reset_game(self):
        self.start_tile = copy.deepcopy(self.start_tile_copy)
        self.current_tile = self.start_tile
        self.targets = copy.deepcopy(self.targets_copy)

    def is_done(self):
        return len(self.get_targets()) == 0

    def go(self, direction):
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        if tile is None or tile.get_type() is TileType.BLOCKED:
            return -1

        # Tile is safe to move to
        self.current_tile = tile
        if not self.is_done() and self.check_for_target():
            return 1
        return 0
