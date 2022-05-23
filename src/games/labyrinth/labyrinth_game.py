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

    @staticmethod
    def setup_game():
        """Factory Method"""
        maze = Labyrinth.create_from("./games/labyrinth/test_labyrinth.json")
        return LabyrinthGame(maze)

    def get_current_tile(self):
        return self.current_tile

    def get_tiles(self):
        return self.labyrinth.get_tiles()

    def get_targets(self):
        return self.labyrinth.get_targets()

    def get_current_target(self):
        return self.get_targets()[-1]

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
        maze = Labyrinth.create_from("./games/labyrinth/test_labyrinth.json")
        self.__init__(maze)

    def is_done(self):
        return len(self.labyrinth.get_targets()) == 0

    def go(self, direction):
        print(direction)
        tile = self.labyrinth.get_neighbor_tile(self.get_current_tile(), direction)
        if not tile or tile.get_type() == TileType.BLOCKED:
            return TileType.BLOCKED

        self.current_tile = tile
        if self.check_current_for_target():
            self.collect_target()
            return TileType.TARGET
        return TileType.EMPTY