# initialize filter
# set open/closed
# depth first search
# printing the result

import pprint
import colorama
import random

LENGTH = 10
PERC_PROB = 0.5

DIRECTIONS = {
    'N': (1, 0),
    'E': (0, 1),
    'S': (-1, 0),
    'W': (0, -1)}
OPEN_CLOSED_MAPPING = {True: 'open', False: 'closed'}
OPEN_FULL_MAPPING = {True: 'full', False: 'empty'}

CHARACTER_MAPPING = {
    'closed': {'empty': 'X', 'full': 'X'},
    'open': {'empty': ' ', 'full': 'F'}
}


# Define a Grid
def create_empty_filter(length=5):
    # f = [
    # [False for x in range(length)]
    # for y in range(length)]
    f = []
    for j in range(LENGTH):
        tmp = []
        for i in range(LENGTH):
            tmp.append(False)
        f.append(tmp)
    return f


def is_open():
    prob = random.random()
    return prob < PERC_PROB


def set_open_closed(empty_filter):
    for j in range(len(empty_filter)):
        for i in range(len(empty_filter[j])):
            empty_filter[j][i] = is_open()
    return empty_filter


def search(filled_filter):
    queue = [(0, x) for x in range(len(filled_filter[0])) if filled_filter[0][x] == True]
    visited = create_empty_filter(LENGTH)
    while queue:
        current_node_index = queue.pop()
        visited[current_node_index[0]][current_node_index[1]] = True
        for direction in DIRECTIONS:
            offset = DIRECTIONS[direction]
            next_offset = (
                current_node_index[0] + offset[0],
                current_node_index[1] + offset[1]
            )
            if 0 < next_offset[0] < LENGTH and 0 < next_offset[1] < LENGTH and \
                    not visited[next_offset[0]][next_offset[1]] and \
                    filled_filter[next_offset[0]][next_offset[1]]:
                queue.insert(0, next_offset)
    return visited


def filter_print(open_closed_filter, fill_filter):
    for j in range(LENGTH):
        line = ''
        for i in range(LENGTH):
            line += '{} '.format(
                CHARACTER_MAPPING[
                    OPEN_CLOSED_MAPPING[
                        open_closed_filter[j][i]]
                ][
                    OPEN_FULL_MAPPING[
                        fill_filter[j][i]
                    ]
                ]
            )
        print(line)


f = create_empty_filter(LENGTH)
# pprint.pprint(f)
f = set_open_closed(f)
pprint.pprint(f)
v = search(f)
filter_print(f, v)
