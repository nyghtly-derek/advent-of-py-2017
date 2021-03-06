"""
--- Problem 3A ---
ou come across an experimental new kind of memory stored on an infinite two-dimensional grid.

Each square on the grid is allocated in a spiral pattern starting at a location marked 1 and then counting up while spiraling outward. For example, the first few squares are allocated like this:

17  16  15  14  13
18   5   4   3  12
19   6   1   2  11
20   7   8   9  10
21  22  23---> ...

While this is very space-efficient (no squares are skipped), requested data must be carried back to square 1 (the location of the only access port for this memory system) by programs that can only move up, down, left, or right. They always take the shortest path: the Manhattan Distance between the location of the data and square 1.

For example:

    Data from square 1 is carried 0 steps, since it's at the access port.
    Data from square 12 is carried 3 steps, such as: down, left, left.
    Data from square 23 is carried only 2 steps: up twice.
    Data from square 1024 must be carried 31 steps.

How many steps are required to carry the data from the square identified in your puzzle input all the way to the access port?
"""

import math

level_totals = {
    0: 1,
}

def get_highest_num(level) -> int:
    """ recursively builds a dictionary of the highest numbers for each level """
    if level in level_totals:
        return level_totals[level]
    else:
        return get_highest_num(level - 1) + (level * 8)

def get_level(num) -> int:
    """ calculates which level a number is in """
    level = 0
    while True:
        if num <= get_highest_num(level):
            return level
        level += 1

def get_row_length(level) -> int:
    """ returns the length of one side in given level """
    if level == 0:
        return 1
    else:
        return level * 2 + 1

def get_corner_cases(level) -> []:
    """ returns a list of all corner cases for a given level in descending order """
    corner_diff = get_row_length(level) - 1
    highest_num = get_highest_num(level)
    a = highest_num
    b = highest_num - corner_diff
    c = highest_num - corner_diff * 2
    d = highest_num - corner_diff * 3
    return [a, b, c, d]


def get_middle_case(num, level):
    """ returns a tuple with the steps to the nearest middle case and the number of that case """
    corner_cases = get_corner_cases(level)
    row_length = get_row_length(level)
    translation_to_middle = math.floor(row_length/2)
    if num <= corner_cases[0] and num >= corner_cases[1]:
        target = corner_cases[0] - translation_to_middle
        steps = abs(target - num)
        return (steps, target)
    if num <= corner_cases[1] and num >= corner_cases[2]:
        target = corner_cases[1] - translation_to_middle
        steps = abs(target - num)
        return (steps, target)
    if num <= corner_cases[2] and num >= corner_cases[3]:
        target = corner_cases[2] - translation_to_middle
        steps = abs(target - num)
        return (steps, target)
    if num <= corner_cases[3]:
        target = corner_cases[3] - translation_to_middle
        steps = abs(target - num)
        return (steps, target)
    return (-1, -1)


def get_steps_to_base(num) -> int:
    """ caculates the number of steps it will take to get to the base case """
    steps = 0
    level = get_level(num)
    if level == 0:
        return steps 
    else:
        steps += get_middle_case(num, level)[0]
        steps += level
        return steps

def print_info(num):
    """ prints infromation on a given number """
    level = get_level(num)
    highest_num = get_highest_num(level)
    row_length = get_row_length(level)
    steps_to_base = get_steps_to_base(num)
    print("for num {}:"
          "\n\t level is {},"
          "\n\t highest num for that level is {},"
          "\n\t row_length is {},"
          "\n\t steps_to_base is {},"
            .format(num, level, highest_num, row_length, steps_to_base))


#print_info(1)
#print_info(12)
#print_info(23)
#print_info(1024)
print_info(325489)
