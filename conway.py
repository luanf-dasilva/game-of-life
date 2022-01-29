import itertools
from random import randrange

def random_init(width: int, height: int, scale: int) -> set:
    return_set = set()
    rows = int(height / scale)
    columns = int(width / scale)
    grid_total = columns * rows
    max_point = randrange(1, grid_total)
    for _ in range(max_point):
        x =   randrange(1, rows)
        y =  randrange(1, columns)
        return_set.add( (x, y) )
    return return_set

def neighbors(point : tuple):
    x, y = point
    yield x + 1, y
    yield x - 1, y
    yield x, y + 1
    yield x, y - 1
    yield x + 1, y + 1
    yield x + 1, y - 1
    yield x - 1, y + 1
    yield x - 1, y - 1

def advance(board: list):
    newstate = set()
    recalc = board | set(itertools.chain(*map(neighbors, board)))
    for point in recalc:
        count = sum((neigh in board) for neigh in neighbors(point))
        if count == 3 or (count == 2 and point in board):
            newstate.add(point)
    return newstate

def run_gol(initial_cond : list, n : int ) -> None:
    automata = set(initial_cond)
    for _ in range(n):
        automata = advance(automata)
        yield automata