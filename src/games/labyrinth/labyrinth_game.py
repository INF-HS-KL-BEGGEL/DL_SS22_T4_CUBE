from games.labyrinth.labyrinth import Labyrinth, Tile


class LabyrinthGame:

    def __init__(self, labyrinth, start_pos: tuple, target_positions: list):
        self.labyrinth = labyrinth
        self.current_position = (0, 0)
        self.start_position = (0, 0)
        self.targets = [(1, 1), (2, 1)]

    @staticmethod
    def setup_game(self):
        """Factory Method"""
        l = Labyrinth.create_from("./src/games/labyrinth/test_labyrinth.json")
        return LabyrinthGame(l, (0, 0), [(4, 4), (4, 3)])

    def go_left(self):
        self.__go(0)

    def go_right(self):
        self.__go(2)

    def go_straight(self):
        self.__go(1)

    def go_back(self):
        self.__go(3)

    def __go(self, direction):
        x, y = self.current_position
        tile = self.labyrinth.get_neigbors(x, y)[direction]

        if self.labyrinth.is_empty_tile(x, y):
            self.current_position = tile.get_pos()

    def is_left_executable(self):
        x, y = self.current_position
        tile = self.labyrinth.get_neigbors(x, y)[0]
        t_x, t_y = tile.get_pos()
        return self.labyrinth.is_empty_tile(t_x, t_y)

    def is_right_executable(self):
        x, y = self.current_position
        tile = self.labyrinth.get_neigbors(x, y)[2]
        t_x, t_y = tile.get_pos()
        return self.labyrinth.is_empty_tile(t_x, t_y)

    def is_straight_executable(self):
        x, y = self.current_position
        tile = self.labyrinth.get_neigbors(x, y)[1]
        t_x, t_y = tile.get_pos()
        return self.labyrinth.is_empty_tile(t_x, t_y)

    def is_back_executable(self):
        x, y = self.current_position
        tile = self.labyrinth.get_neigbors(x, y)[3]
        t_x, t_y = tile.get_pos()
        return self.labyrinth.is_empty_tile(t_x, t_y)

    def reset_game(self):
        self.current_position = (0, 0)

    def is_done(self):
        return len(self.targets) == 0
