"""
Containers are objects that implements a __contains__ method.

The in statement in python:

    element in container

becomes:

    container.__contains__(element)
"""

# Less pythonic approach of marking a coordinate on a 2d map.
def mark_coordinate(grid, coord):
    if 0 <= coord.x < grid.width and 0 <= coord.y < grid.height:
        grid[coord] = True


class Boundaries:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __contains__(self, coord):
        x, y = coord
        return 0 <= x < self.width and 0 <= y <= self.height


class Grid:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.limits = Boundaries(width, height)

    def __contains__(self, coord):
        return coord in self.limits


# Pythonic-approach.
def mark_coordinate(grid, coord):
    if coord in grid:
        grid[coord] = True
