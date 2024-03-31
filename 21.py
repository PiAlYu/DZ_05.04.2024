from functools import lru_cache
def moves(h):
    return h + 10, h * 2
@lru_cache(None)
def game(h):
    if h >= 82:
        return 'end'
    if all(game(i) == 'end' for i in moves(h)):
        return 'p1'
    if any(game(i) == 'p1' for i in moves(h)):
        return 'v1'
    if all(game(i) == 'v1' or game(i) == 'end' for i in moves(h)):
        return 'p2'
    if any(game(i) == 'p2' or game(i) == 'p1' for i in moves(h)):
        return 'v2'

for i in range(1, 81):
    if game(i) == 'v2':
        print(i)
        break