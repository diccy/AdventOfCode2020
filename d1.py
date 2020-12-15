
def Resolve(do_print = False):

    with open('d1.txt', 'r') as f:
        content = [int(s) for s in f.read().splitlines()]

    numbers = [False] * 2020
    for n in content:
        numbers[n] = True

    def PartOne():
        for n in content:
            diff = 2020 - n
            if diff > 0 and numbers[diff]:
                return n * diff

    def PartTwo():
        for i, n in enumerate(content[:-1]):
            for m in content[i+1:]:
                diff = 2020 - (n + m)
                if diff > 0 and numbers[diff]:
                    return n * m * diff

    bg1 = PartOne()
    bg2 = PartTwo()
    if do_print:
        print('Bon gaulois 1:', bg1)
        print('Bon gaulois 2:', bg2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 988771
    #   2: 171933104
