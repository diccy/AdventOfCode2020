import numpy

S_EMPTY = ord('.')
S_FREE = ord('L')
S_OCCUPIED = ord('#')
STATES = {
    ord('.'): S_EMPTY,
    ord('L'): S_FREE,
    ord('#'): S_OCCUPIED,
}

with open("d11.txt", "r") as f:
    content = f.read().splitlines()

w = len(content[0])
h = len(content)

seats = None

def InitSeatsFromContent():
    global seats
    seats = numpy.zeros((w, h, 2), dtype=int)
    y = 0
    for l in content:
        x = 0
        for c in l:
            state = STATES.get(ord(c))
            seat = seats[x, y]
            seat[0] = state
            seat[1] = state
            x +=1
        y += 1

dirs = ((-1,-1), ( 0,-1), ( 1,-1),
        (-1, 0),          ( 1, 0),
        (-1, 1), ( 0, 1), ( 1, 1))
def OccupiedNeighboursCount1(x0, y0, i):
    count = 0
    for dir in dirs:
        x = x0 + dir[0]
        y = y0 + dir[1]
        if 0 <= x and x < w and 0 <= y and y < h:
            if seats[x, y, i] == S_OCCUPIED:
                count += 1
    return count

def OccupiedNeighboursCount2(x0, y0, i):
    count = 0
    for dir in dirs:
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

def Resolve(part):
    print("Part", part, "...")
    
    # occupied seats to free
    osf = (4, 5)[part-1]
    # occupied neighbours count function
    onc = (OccupiedNeighboursCount1, OccupiedNeighboursCount2)[part-1]

    InitSeatsFromContent()
    
    n = 0 # next overall state id
    p = 1 # previous overall state id
    it = 0
    occupied_seats = 0
    while True:
        it += 1
        changes = 0
        occupied_seats = 0
        y = 0
        while y < h:
            x = 0
            while x < w:
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
                x +=1
            y += 1
        
        if changes == 0:
            break
        p, n = n, p

    print("Sieges gaulois", part, ":", occupied_seats, " ( it:", it, ")")

Resolve(1)
Resolve(2)
