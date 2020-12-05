with open("d5.txt", "r") as f:
    content = f.read().splitlines()

lowest = 128 * 8
highest = 0
occupied_seats_sum = 0
for line in content:
    row = 0
    col = 0
    for i in range(0, 7):
        if line[i] == 'B':
            row = row + (1 << (6 - i))
    for i in range(7, 10):
        if line[i] == 'R':
            col = col + (1 << (9 - i))
    id = row * 8 + col
    occupied_seats_sum += id
    lowest = min(lowest, id)
    highest = max(highest, id)

overall_sum = ((highest * (highest + 1)) - (lowest * (lowest - 1))) // 2
seat = overall_sum - occupied_seats_sum

print("Highest gaulois:", highest)
print("Siege gaulois:", seat)
