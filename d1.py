from copy import copy

map = {}
with open("d1.txt", "r") as f:
    for s in f.read().splitlines():
        map[int(s)] = True

def PartOne(map):
    for n in map.keys():
        diff = 2020 - n
        if map.get(diff) != None:
            print("Bon gaulois 1:", n * diff)
            return

def PartTwo(map):
    nit = iter(map)
    while True:
        try:
            n = next(nit)
            mit = copy(nit)
            while True:
                try:
                    m = next(mit)
                    diff = 2020 - (n + m)
                    if map.get(diff) != None:
                        print("Bon gaulois 2:", n * m * diff)
                        return
                except StopIteration:
                    break
        except StopIteration:
            break

PartOne(map)
PartTwo(map)
