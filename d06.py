
from collections import Counter

def Resolve(do_print = False):

    with open('d06.txt', 'r') as f:
        content = [entry.splitlines() for entry in f.read().split('\n\n')]

    ORD_A = ord('a')

    sum1 = 0
    sum2 = 0
    for entry in content:
        answers = [0] * 26
        for line in entry:
            for c in line:
                answers[ord(c) - ORD_A] += 1
        for n in answers:
            if n > 0:
                sum1 += 1
                if n == len(entry): sum2 += 1

    if do_print:
        print('Somme gauloise 1:', sum1)
        print('Somme gauloise 2:', sum2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 6249
    #   2: 3103
