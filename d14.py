from time import time
from math import log2

with open("d14.txt", "r") as f:
    content = f.read().splitlines()

memory1 = {}
memory2 = {}
mask_0, mask_1, mask_X = 0, 0, 0
list_X = []
for line in content:
    if line[:2] == 'ma':
        mask_0, mask_1, mask_X = 0, 0, 0
        list_X = []
        i = 0
        while i < 36:
            c = line[7+i]
            if c == '0':
                mask_0 |= 1 << (35 - i)
            elif c == '1':
                mask_1 |= 1 << (35 - i)
            else:
                mask_X |= 1 << (35 - i)
                list_X.insert(0, 35 - i)
            i += 1
    else:
        end_mem = line.find(']', 4)
        mem1 = int(line[4:end_mem])
        val = int(line[end_mem+4:])
        # Part 1
        memory1[mem1] = (val | mask_1) & (~mask_0)
        # Part 2
        mem2 = mem1 | mask_1
        if mask_X == 0:
            memory2[mem2] = val
        else:
            i = 0
            count = 2 ** len(list_X)
            while i < count:
                val_X = 0
                j = i
                while j > 0:
                    b = int(log2(j & -j))
                    val_X |= 1 << list_X[b]
                    j &= ~(1 << b)
                mem2 = val_X | (mem2 & (~mask_X))
                memory2[mem2] = val
                i += 1

print("Somme gauloise 1:", sum(memory1.values()))
print("Somme gauloise 2:", sum(memory2.values()))
