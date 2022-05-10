import random
import json

class Tile:

    def __init__(self, type, x, y):
        self.type = type
        self.x = x
        self.y = y

    def get_type(self):
        return self.type

    def get_pos(self):
        return self.x, self.y


class Labyrinth:

    def __init__(self, map):
        self.map = map

    def add_target(self):
        pass

    def remove_target(self):
        pass

    def get_tile(self, x, y):
        pass

    def is_empty_tile(self, x, y):
        """ If position is not blocked"""
        return Tile("empty").get_type() == "empty"

    def is_blocked_tile(self, x, y):
        pass

    def get_neigbors(self, x, y):
        """
        index 0: left
        index 1: straight
        index 2: right
        index 3: beck
        :param x:
        :param y:
        :return:
        """
        pass

    @staticmethod
    def create(self, size, seed):
        """
        create Labyrnith random from given seed
        :param self:
        :param size:
        :param seed:
        :return:
        """
        pass

    @staticmethod
    def create_from(self, filename):
        """
        Factory Method to create Labyrinth from definition file
        :param self:
        :param filename:
        :return:
        """
        map = []

        mapping = {
            "*": "empty",
            "x": "blocked",
            "s": "start",
            "t": "target"
        }
        data = json.load(open(filename, "rb"))

        for y, row in enumerate(data["tiles"]):
            map_tmp_row = []
            for x, tile in enumerate(row):
                map_tmp_row.append(Tile(mapping[tile], x, y))
            map.append(map_tmp_row)

        return Labyrinth(map)