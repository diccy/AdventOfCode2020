with open("d1.txt", "r") as f:
    content = [int(s) for s in f.read().splitlines()]

numbers = [False] * 2020
for n in content:
    numbers[n] = True

def PartOne():
    for n in content:
        diff = 2020 - n
        if diff > 0 and numbers[diff]:
            print("Bon gaulois 1:", n * diff)
            return

def PartTwo():
    i = 0
    for n in content[:-1]:
        i += 1
        for m in content[i:]:
            diff = 2020 - (n + m)
            if diff > 0 and numbers[diff]:
                print("Bon gaulois 2:", n * m * diff)
                return

PartOne()
PartTwo()
