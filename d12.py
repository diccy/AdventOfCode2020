
def Resolve(do_print = False):

    with open('d12.txt', 'r') as f:
        content = [(ord(line[0]), int(line[1:])) for line in f.read().splitlines()]

    #        East    South    West     North
    DIRS = ((1, 0), (0, -1), (-1, 0), (0, 1))

    # Part 1

    ship_dir_id = 0
    shipx, shipy = 0, 0

    def RotateShipDir(n):
        nonlocal ship_dir_id
        ship_dir_id = (ship_dir_id + (n // 90)) % 4
        return ship_dir_id

    DIRS_SWITCH = {
        ord('E'): lambda n: (0, n),
        ord('S'): lambda n: (1, n),
        ord('W'): lambda n: (2, n),
        ord('N'): lambda n: (3, n),
        ord('F'): lambda n: (ship_dir_id, n),
        ord('R'): lambda n: (RotateShipDir( n), 0),
        ord('L'): lambda n: (RotateShipDir(-n), 0),
    }

    for c, n in content:
        dir_id, factor = DIRS_SWITCH.get(c)(n)
        dx, dy = DIRS[dir_id]
        shipx += dx * factor
        shipy += dy * factor

    dg1 = abs(shipx) + abs(shipy)


    # Part 2

    shipx, shipy = 0, 0
    wpx, wpy = 10, 1

    Rotate = lambda a, b, d: ((a, b), (b, -a), (-a, -b), (-b, a))[(d // 90) % 4]

    def MoveShip(factor):
        nonlocal shipx, shipy
        shipx += wpx * factor
        shipy += wpy * factor

    def MoveWaypoint(dx, dy, factor):
        nonlocal wpx, wpy
        wpx += dx * factor
        wpy += dy * factor

    def RotateWaypoint(degrees):
        nonlocal wpx, wpy
        wpx, wpy = Rotate(wpx, wpy, degrees)

    ACTIONS_SWITCH = {
        ord('E'): lambda n: MoveWaypoint(1, 0, n),
        ord('S'): lambda n: MoveWaypoint(0, -1, n),
        ord('W'): lambda n: MoveWaypoint(-1, 0, n),
        ord('N'): lambda n: MoveWaypoint(0, 1, n),
        ord('F'): lambda n: MoveShip(n),
        ord('R'): lambda n: RotateWaypoint( n),
        ord('L'): lambda n: RotateWaypoint(-n),
    }

    for c, n in content:
        ACTIONS_SWITCH.get(c)(n)

    dg2 = abs(shipx) + abs(shipy)


    if do_print:
        print('Distance gauloise 1:', dg1)
        print('Distance gauloise 2:', dg2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 1687
    #   2: 20873
