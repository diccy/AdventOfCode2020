
def Resolve(do_print = False):

    with open('d18.txt', 'r') as f:
        content = f.read().replace(' ', '').splitlines()

    ORD_0  = ord('0')
    ORD_P  = ord('+')
    ORD_M  = ord('*')
    ORD_PO = ord('(')
    ORD_PC = ord(')')
    OP_P = lambda a, b: a + b
    OP_M = lambda a, b: a * b

    #              +  *
    PRIORITIES1 = (1, 1)
    PRIORITIES2 = (2, 1)

    def Evaluate(line, prio):
        values = []
        ops = []
        for c in line:
            o = ord(c)
            if o == ORD_P or o == ORD_M:
                op, p = (OP_P, prio[0]) if o == ORD_P else (OP_M, prio[1])
                while len(ops) > 0 and ops[-1][1] >= p:
                    values.append(ops.pop()[0](values.pop(), values.pop()))
                ops.append((op, p))
            elif o == ORD_PO:
                ops.append((ORD_PO, 0))
            elif o == ORD_PC:
                while ops[-1][0] != ORD_PO:
                    values.append(ops.pop()[0](values.pop(), values.pop()))
                ops.pop()
            else:
                values.append(o - ORD_0)

        while len(values) > 1:
            values.append(ops.pop()[0](values.pop(), values.pop()))
        return values[0]

    sum1 = 0
    sum2 = 0
    for line in content:
        sum1 += Evaluate(line, PRIORITIES1)
        sum2 += Evaluate(line, PRIORITIES2)

    if do_print:
        print('Somme gauloise 1:', sum1)
        print('Somme gauloise 2:', sum2)

# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 36382392389406
    #   2: 381107029777968
