
def Resolve(do_print = False):

    I_ACC = 0
    I_JMP = 1
    I_NOP = 2
    INSTRUCTIONS = {
        'acc': I_ACC,
        'jmp': I_JMP,
        'nop': I_NOP,
    }

    with open('d08.txt', 'r') as f:
        content = [(INSTRUCTIONS.get(line[:3]), int(line[3:])) for line in f.read().splitlines()]

    l = len(content)

    # Part 1

    ran = [False] * l
    i = 0
    acc1 = 0
    while i < l:
        if ran[i]:
            break
        instruction, n = content[i]
        ran[i] = True
        if instruction == I_ACC:
            acc1 += n
            i += 1
        elif instruction == I_JMP:
            i += n
        elif instruction == I_NOP:
            i += 1

    # Part 2

    ran = [False] * l
    change = -1
    i = 0
    acc2 = 0

    def ApplyInstruction(iid, do, sign):
        nonlocal i
        nonlocal acc2
        instruction, n = content[iid]
        if iid == change:
            instruction = I_JMP if instruction == I_NOP else I_NOP
        ran[iid] = do
        if instruction == I_ACC:
            acc2 = acc2 + n * sign
            i += sign
        elif instruction == I_JMP:
            i += n * sign
        elif instruction == I_NOP:
            i += sign
        return instruction

    track = []
    while i < l:
        if ran[i]:
            if change != -1:
                while i != change:
                    ApplyInstruction(track.pop(), False, -1)
                ApplyInstruction(track.pop(), False, -1)
            while len(track) > 0:
                iid = track.pop()
                instruction = ApplyInstruction(iid, False, -1)
                if instruction == I_JMP or instruction == I_NOP:
                    change = iid
                    break
        track.append(i)
        ApplyInstruction(i, True, 1)

    if do_print:
        print('Accumulator gaulois 1:', acc1)
        print('Accumulator gaulois 2:', acc2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 1928
    #   2: 1319
