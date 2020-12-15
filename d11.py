import numpy

def Resolve(do_print = False):

    with open('d11.txt', 'r') as f:
        content = f.read().splitlines()

    S_EMPTY = ord('.')
    S_FREE = ord('L')
    S_OCCUPIED = ord('#')
    STATES = {
        ord('.'): S_EMPTY,
        ord('L'): S_FREE,
        ord('#'): S_OCCUPIED,
    }

    DIRS = ((-1,-1), ( 0,-1), ( 1,-1),
            (-1, 0),          ( 1, 0),
            (-1, 1), ( 0, 1), ( 1, 1))

    w = len(content[0])
    h = len(content)

    seats = None

    def InitSeatsFromContent():
        nonlocal seats
        seats = numpy.zeros((w, h, 2), dtype=int)
        for y, line in enumerate(content):
            for x, c in enumerate(line):
                state = STATES.get(ord(c))
                seats[x, y] = (state, state)

    def OccupiedNeighboursCount1(x0, y0, i):
        count = 0
        for dir in DIRS:
            x = x0 + dir[0]
            y = y0 + dir[1]
            if 0 <= x and x < w and 0 <= y and y < h:
                if seats[x, y, i] == S_OCCUPIED:
                    count += 1
        return count

    def OccupiedNeighboursCount2(x0, y0, i):
        count = 0
        for dir in DIRS:
            x, y = x0, y0
            while True:
                x += dir[0]
                y += dir[1]
                if 0 <= x and x < w and 0 <= y and y < h:
                    state = seats[x, y, i]
                    if state != S_EMPTY:
                        if state == S_OCCUPIED:
                            count += 1
                        break
                else:
                    break
        return count

    def Part(part):

        # occupied seats to free
        osf = (4, 5)[part-1]
        # occupied neighbours count function
        onc = (OccupiedNeighboursCount1, OccupiedNeighboursCount2)[part-1]

        InitSeatsFromContent()

        n = 0 # next overall state id
        p = 1 # previous overall state id
        occupied_seats = 0
        while True:
            changes = 0
            occupied_seats = 0
            for y in range(h):
                for x in range(w):
                    state = seats[x, y, p]
                    if state == S_FREE:
                        if onc(x, y, p) == 0:
                            state = S_OCCUPIED
                            changes += 1
                    elif state == S_OCCUPIED:
                        if onc(x, y, p) >= osf:
                            state = S_FREE
                            changes += 1
                    seats[x, y, n] = state
                    if state == S_OCCUPIED:
                        occupied_seats += 1

            if changes == 0:
                break
            p, n = n, p

        if do_print:
            print(f'Sieges gaulois {part}: {occupied_seats}')

    Part(1)
    Part(2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 2222
    #   2: 2032
