with open("d10.txt", "r") as f:
    content = [int(s) for s in f.read().splitlines()]

content.append(0) # add charging outlet
content.sort()

diffs = [0, 0, 1] # device has a built-in joltage adapter rated for 3 jolts higher than the highest-rated adapter

sums_fifo = [0, 0, 1]
diff1suite = 0

l = len(content)
i = 0
while i < l - 1:
    d = content[i+1] - content[i]
    diffs[d - 1] += 1
    if d == 1:
        diff1suite += 1
    else:
        diff1suite = 0
    if diff1suite > 2:
        sums_fifo.append(sums_fifo[0] + sums_fifo[1] + sums_fifo[2])
    elif diff1suite == 2:
        sums_fifo.append(sums_fifo[1] + sums_fifo[2])
    elif diff1suite <= 1:
        sums_fifo.append(sums_fifo[2])
    sums_fifo.pop(0)
    i += 1

print("Diffs gauloises 1:", diffs[0] * diffs[2])
print("Arrangements gaulois 2:", sums_fifo[2])
