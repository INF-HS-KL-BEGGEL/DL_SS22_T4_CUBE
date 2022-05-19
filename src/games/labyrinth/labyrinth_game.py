from games.labyrinth.labyrinth import Direction, Labyrinth, Tile, TileType
from games.game import Game
from games.labyrinth.actions import GoAction
import copy


class LabyrinthGame(Game):

    def __init__(self, labyrinth):
        super().__init__()
        self.labyrinth = labyrinth
        self.current_tile = self.labyrinth.get_tile(0, 0)
        self.start_tile = self.labyrinth.get_tile(0, 0)
        self.targets = [Tile(TileType.TARGET, 2, 1)]

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
        maze = Labyrinth.create_from("./src/games/labyrinth/test_labyrinth.json")
        return LabyrinthGame(maze)

    def is_accessible(self, direction):
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        return self.labyrinth.is_accessible_tile(tile)

    def reset_game(self):
        self.start_tile = copy.deepcopy(self.start_tile_copy)
        self.current_tile = self.start_tile
        self.targets = copy.deepcopy(self.targets_copy)

    def is_done(self):
        return len(self.targets) == 0

    def go(self, direction):
        print(direction)
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        if not tile:
            return -1
        self.current_tile = tile
        if self.check_for_target():
            return 1
        return 0
