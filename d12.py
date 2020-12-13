with open("d12.txt", "r") as f:
    content = f.read().splitlines()

#        East    South    West     North
DIRS = [(1, 0), (0, -1), (-1, 0), (0, 1)]


# Part 1

ship_dir_id = 0
ship_pos = [0, 0]

def RotateShipDir(n):
    global ship_dir_id
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

for line in content:
    dir_char = line[0]
    value = int(line[1:])
    dir_id, factor = DIRS_SWITCH.get(ord(dir_char))(value)
    dir = DIRS[dir_id]
    ship_pos[0] += dir[0] * factor
    ship_pos[1] += dir[1] * factor

print("Distance gauloise 1:", abs(ship_pos[0]) + abs(ship_pos[1]))


# Part 2

ship_pos = [0, 0]
wp_pos = [10, 1]

def MoveShip(factor):
    ship_pos[0] += wp_pos[0] * factor
    ship_pos[1] += wp_pos[1] * factor

def MoveWaypoint(dir, factor):
    wp_pos[0] += dir[0] * factor
    wp_pos[1] += dir[1] * factor

def RotateWaypoint(degrees):
    rotate = lambda a, b, i: ((a, b), (b, -a), (-a, -b), (-b, a))[i]
    wp_pos[0], wp_pos[1] = rotate(wp_pos[0], wp_pos[1], (4 + (degrees // 90)) % 4)

ACTIONS_SWITCH = {
    ord('E'): lambda n: MoveWaypoint(DIRS[0], n),
    ord('S'): lambda n: MoveWaypoint(DIRS[1], n),
    ord('W'): lambda n: MoveWaypoint(DIRS[2], n),
    ord('N'): lambda n: MoveWaypoint(DIRS[3], n),
    ord('F'): lambda n: MoveShip(n),
    ord('R'): lambda n: RotateWaypoint( n),
    ord('L'): lambda n: RotateWaypoint(-n),
}

for line in content:
    dir_char = line[0]
    value = int(line[1:])
    ACTIONS_SWITCH.get(ord(dir_char))(value)

print("Distance gauloise 2:", abs(ship_pos[0]) + abs(ship_pos[1]))
