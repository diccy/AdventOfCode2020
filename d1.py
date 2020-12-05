with open("d1.txt", "r") as f:
    content = [int(s) for s in f.read().splitlines()]

l = len(content)

def PartOne(content, l):
    for i in range(0, l-1):
        for j in range(i+1, l):
            if content[i] + content[j] == 2020:
                print("Bon gaulois 1:", content[i] * content[j])
                return

def PartTwo(content, l):
    for i in range(0, l-2):
        for j in range(i+1, l-1):
            for k in range(j+1, l):
                if content[i] + content[j] + content[k] == 2020:
                    print("Bon gaulois 2:", content[i] * content[j] * content[k])
                    return

PartOne(content, l)
PartTwo(content, l)
