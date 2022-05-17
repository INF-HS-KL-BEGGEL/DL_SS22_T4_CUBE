from os import access
import random
import json
from enum import Enum
from turtle import width


class TileType(Enum):
    EMPTY = 0
    BLOCKED = 1
    START = 2
    TARGET = 3

class Direction(Enum):
    NORTH = 0
    EAST = 1
    SOUTH = 2
    WEST = 3

class Tile:

    def __init__(self, tile_type, x, y):
        self.tile_type = tile_type
        self.x = x
        self.y = y

    def get_type(self):
        return self.tile_type

    def get_pos(self):
        return self.x, self.y


class Labyrinth:

    def __init__(self, maze_map):
        self.maze_map = maze_map
        # the number of rows
        self.height = len(maze_map)
        # the number of columns
        self.width = len(self.maze_map[0])

    def get_maze_map(self):
        return self.maze_map
    
    def get_tile(self, x, y):
        return self.maze_map[x][y]           

    def get_all_accessible_tiles(self):
        accessible_tiles = []
        maze = self.get_maze_map()
        for row in maze:
            for tile in row: 
                if tile.get_type() != TileType.BLOCKED:
                    accessible_tiles.append(tile)
        return accessible_tiles

    def is_accessible_tile(self, tile):
        """ If position is not blocked"""
        if tile is None:
            return False
        return tile.get_type() == TileType.EMPTY

    def is_blocked_tile(self, tile):
        return tile.get_type() == TileType.BLOCKED

    def get_west_tile(self, tile):
        x, y = tile.get_pos()
        if (y - 1) > 0:
            return self.get_tile(x, y - 1)
        return None

    def get_east_tile(self, tile):
        x, y = tile.get_pos()
        if (y + 1) < self.width:
            return self.get_tile(x, y + 1)
        return None
    
    def get_north_tile(self, tile):
        x, y = tile.get_pos()
        if (x - 1) > 0:
            return self.get_tile(x - 1, y)
        return None
    
    def get_south_tile(self, tile):
        x, y = tile.get_pos()
        if (x + 1) < self.height:
            return self.get_tile(x + 1, y)
        return None

    def get_neighbor_tile(self, tile, direction):
        if direction == Direction.NORTH:
            return self.get_north_tile(tile)
        elif direction == Direction.EAST:
            return self.get_east_tile(tile)
        elif direction == Direction.SOUTH:
            return self.get_south_tile(tile)
        elif direction == Direction.WEST:
            return self.get_west_tile(tile)
        return None

    @staticmethod
    def create_random(self, seed):
        """
        :param seed:
        :return:
        """
        pass

    @staticmethod
    def create_from(filename):
        """
        Factory Method to create Labyrinth from definition file
        :param self:
        :param filename:
        :return:
        """
        maze_map = []

        mapping = {
            "o": TileType.EMPTY,
            "#": TileType.BLOCKED,
            "s": TileType.START,
            "x": TileType.TARGET
        }
        data = json.load(open(filename, "rb"))

        for y, row in enumerate(data["tiles"]):
            map_tmp_row = []
            for x, tile in enumerate(row):
                map_tmp_row.append(Tile(mapping[tile], x, y))
            maze_map.append(map_tmp_row)

        return Labyrinth(maze_map)