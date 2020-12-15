
def Resolve(do_print = False):

    with open('d8.txt', 'r') as f:
        content = f.read().splitlines()

    l = len(content)

    I_ACC = 0
    I_JMP = 1
    I_NOP = 2
    INSTRUCTIONS = {
        'acc': I_ACC,
        'jmp': I_JMP,
        'nop': I_NOP,
    }

    # Part 1

    ran = [False] * l
    i = 0
    acc1 = 0
    while i < l:
        if ran[i]:
            break
        line = content[i]
        instruction = INSTRUCTIONS.get(line[:3])
        n = int(line[3:])
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
    track = []
    change = -1
    i = 0
    acc2 = 0

    def ApplyInstruction(id, do, sign):
        nonlocal ran
        nonlocal i
        nonlocal acc2
        line = content[id]
        instruction = INSTRUCTIONS.get(line[:3])
        if id == change:
            instruction = I_JMP if instruction == I_NOP else I_NOP
        n = int(line[3:])
        ran[id] = do
        if instruction == I_ACC:
            acc2 = acc2 + n * sign
            i += sign
        elif instruction == I_JMP:
            i += n * sign
        elif instruction == I_NOP:
            i += sign
        return (id, instruction)

    def DoInstruction():
        nonlocal track
        track.append(i)
        ApplyInstruction(i, True, 1)

    def UndoInstruction():
        id = track.pop()
        return ApplyInstruction(id, False, -1)

    while i < l:
        if ran[i]:
            if change != -1:
                while i != change:
                    UndoInstruction()
                UndoInstruction()
            while len(track) > 0:
                id, instruction = UndoInstruction()
                if instruction == I_JMP or instruction == I_NOP:
                    change = id
                    break
        DoInstruction()

    if do_print:
        print('Accumulator gaulois 1:', acc1)
        print('Accumulator gaulois 2:', acc2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 1928
    #   2: 1319
