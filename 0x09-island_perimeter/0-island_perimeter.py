#!/usr/bin/python3
""" Module for the island perimerter solution """


def island_perimeter(grid):
    """
    :type grid: List[List[int]]
    :rtype: int
    """
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if grid[i][j] == 1:
                if j == 0:  # check left edge
                    count += 1
                if i == 0:  # check top
                    count += 1
                if j + 1 == len(grid[i]):  # check right edge
                    count += 1
                if i + 1 == len(grid):  # check bottom
                    count += 1

                if i - 1 >= 0:
                    if grid[i - 1][j] == 0:  # check box above
                        count += 1
                if i + 1 < len(grid):
                    if grid[i + 1][j] == 0:  # check box below
                        count += 1

                if j - 1 >= 0:
                    if grid[i][j - 1] == 0:  # check box to the left
                        count += 1
                if j + 1 < len(grid[i]):
                    if grid[i][j + 1] == 0:  # check box to the right
                        count += 1
    return count


# grid = [[0, 1, 0, 0], [1, 1, 1, 0], [0, 1, 0, 0], [1, 1, 0, 0]]
# grid = [[0,0,0,0],[0,0,0,0],[0,0,0,0],[1,0,0,0]]
