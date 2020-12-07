map = {}
with open("d1.txt", "r") as f:
    for s in f.read().splitlines():
        map[int(s)] = True

def PartOne(map):
    for i in map.keys():
        diff = 2020 - i
        if map.get(diff) != None:
            print("Bon gaulois 1:", i * diff)
            return

def PartTwo(map):
    for i in map.keys():
        for j in map.keys():
            diff = 2020 - (i + j)
            if map.get(diff) != None:
                print("Bon gaulois 2:", i * j * diff)
                return

PartOne(map)
PartTwo(map)
