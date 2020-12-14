with open("d14.txt", "r") as f:
    content = f.read().splitlines()

memory1 = {}
memory2 = {}
mask_0 = 0 # set 0
mask_1 = 0 # set 1
mask_X = 0 # set X
mask_X_count = 0 # X count
for line in content:
    if line[:2] == 'ma':
        mask_0 = 0
        mask_1 = 0
        mask_X = 0
        mask_X_count = 0
        i = 0
        while i < 36:
            m = 1 << (35 - i)
            c = line[7+i]
            if c == '0':
                mask_0 |= m
            elif c == '1':
                mask_1 |= m
            else:
                mask_X |= m
                mask_X_count += 1
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
            count = 2 ** mask_X_count
            while i < count:
                i_copy = i
                mask_X_copy = mask_X
                j = 0
                val_X = 0
                while mask_X_copy > 0:
                    if (mask_X_copy & 1) == 1:
                        val_X |= (i_copy & 1) << j
                        i_copy >>= 1
                    mask_X_copy >>= 1
                    j += 1
                masked_mem = val_X | (mem2 & (~mask_X))
                memory2[masked_mem] = val
                i += 1

print("Somme gauloise 1:", sum(memory1.values()))
print("Somme gauloise 2:", sum(memory2.values()))
