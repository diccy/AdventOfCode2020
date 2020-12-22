import math
from collections import deque
import numpy as np

def Resolve(do_print = False):

    with open('d20.txt', 'r') as f:
        content = f.read().split('\n\n')

    w = 0
    def FlipEdge(e):
        n = 0
        for i in range(w):
            n |= (e & 1) << (w - i - 1)
            e >>= 1
        return n

    def RotateSquare(s):
        return (s[1], s[2], s[3], s[0])

    def FlipSquare(s):
        return (FlipEdge(s[0]), FlipEdge(s[3]), FlipEdge(s[2]), FlipEdge(s[1]))

    squares_dict = {}
    squares_content_dict = {}
    edges_dict = {}
    for tile in content:
        desc = tile.split('\n')
        if '' in desc:
            desc.remove('')
        square = int(desc[0][4:-1])
        w = len(desc[1])
        top    = FlipEdge(sum(1 << i if c == '#' else 0 for i, c in enumerate(desc[1])))
        right  = FlipEdge(sum(1 << i if l[-1] == '#' else 0 for i, l in enumerate(desc[1:])))
        bottom = sum(1 << i if c == '#' else 0 for i, c in enumerate(desc[-1]))
        left   = sum(1 << i if l[0] == '#' else 0 for i, l in enumerate(desc[1:]))
        square_edges = (top, right, bottom, left)
        squares_dict[square] = square_edges
        for edge in (top, right, bottom, left, FlipEdge(top), FlipEdge(right), FlipEdge(bottom), FlipEdge(left)):
            if edge in edges_dict:
                edges_dict[edge].append(square)
            else:
                edges_dict[edge] = [square]
        squares_content_dict[square] = np.array([[1 if c == '#' else 0 for c in line[1:-1]] for line in desc[2:-1]], dtype=np.uint8)

    # assuming puzzle is a square
    l = int(math.sqrt(len(squares_dict)))

    grid = [[None for x in range(l)] for y in range(l)]
    available_squares = deque(squares_dict.items())
    def Bt(x, y):
        if x == l:
            return Bt(0, y + 1)
        if y == l:
            return True
        bottom_f = FlipEdge(grid[y-1][x][1][2]) if y > 0 else None
        right_f  = FlipEdge(grid[y][x-1][1][1]) if x > 0 else None
        av_squares_count = len(available_squares)
        while len(available_squares) > 0 and av_squares_count > 0:
            square, edges = available_squares.pop()
            e = edges
            for f in range(2):
                for r in range(4):
                    if (bottom_f == None or e[0] == bottom_f) and (right_f == None or e[3] == right_f):
                        grid[y][x] = (square, e, f, r)
                        if Bt(x + 1, y):
                            return True
                        grid[y][x] = None
                    e = RotateSquare(e)
                e = FlipSquare(e)
            available_squares.appendleft((square, edges))
            av_squares_count -= 1
        return False
    Bt(0, 0)

    # Part 1
    corners_mult  = grid[0][0][0]
    corners_mult *= grid[0][l-1][0]
    corners_mult *= grid[l-1][0][0]
    corners_mult *= grid[l-1][l-1][0]

    # Part 2
    a = np.zeros((l * 8, l * 8), dtype=np.uint8)
    for y, line in enumerate(grid):
        for x, tile in enumerate(line):
            square_content = squares_content_dict[tile[0]]
            if tile[2] > 0:
                square_content = np.fliplr(square_content)
            if tile[3] > 0:
                square_content = np.rot90(square_content, tile[3])
            a[y*8:(y+1)*8, x*8:(x+1)*8] = square_content
    dieses_count = np.sum(a)

    def CountMonsters(a):
        m = np.array([[0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,0],
                      [1,0,0,0,0,1,1,0,0,0,0,1,1,0,0,0,0,1,1,1],
                      [0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,1,0,0,0]], dtype=np.uint8)
        mc = np.sum(m, dtype=np.uint8)
        for _ in range(2):
            for _ in range(4):
                mh, mw = m.shape
                monster_count = 0
                for y in range((l * 8) - mh):
                    for x in range((l * 8) - mw):
                        if mc == np.sum(np.logical_and(a[y:y+mh, x:x+mw], m)):
                            monster_count += 1
                if monster_count > 0:
                    return monster_count, mc
                m = np.rot90(m)
            m = np.fliplr(m)
    monster_count, mc = CountMonsters(a)

    if do_print:
        print('Coins gaulois 1:', corners_mult)
        print('Dieses gaulois 2:', dieses_count - (monster_count * mc))


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 66020135789767
    #   2: 1537
