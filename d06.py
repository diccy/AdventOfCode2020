
def Resolve(do_print = False):

    with open('d06.txt', 'r') as f:
        content = f.read().splitlines()
    content.append('')

    ORD_A = ord('a')

    sum1 = 0
    sum2 = 0
    gaulois = 0
    answers = [0] * 26
    for line in content:
        if len(line) == 0:
            #sum1 += sum(n > 0 for n in answers) # joli mais ca cree une liste?
            #sum2 += sum(n == gaulois for n in answers) # joli mais ca cree une liste?
            for i, n in enumerate(answers):
                if n > 0:
                    sum1 += 1
                    if n == gaulois:
                        sum2 += 1
                    answers[i] = 0
            gaulois = 0
        else:
            gaulois += 1
            for c in line:
                answers[ord(c) - ORD_A] += 1

    if do_print:
        print('Somme gauloise 1:', sum1)
        print('Somme gauloise 2:', sum2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 6249
    #   2: 3103
