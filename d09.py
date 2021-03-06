
def Resolve(do_print = False):

    with open('d09.txt', 'r') as f:
        content = [int(s) for s in f.read().splitlines()]

    bad_roman = 0

    # Part one

    # This solution totally fails at not using the same number twice,
    # and is fucked up if there is 2 or more different entries with the same
    # value, erasing all of them when doing dic.pop(nmp).

    P = 25
    tab = [0] * P
    dic = {}

    for i, n in enumerate(content):
        if i >= P:
            sum = None
            for j in range(P):
                m = tab[j]
                if n - m in dic:
                    sum = (j, m)
                    break
            if sum == None:
                bad_roman = n
                break
            nmp = tab[i % P]
            dic.pop(nmp)
        tab[i % P] = n
        dic[n] = True


    # Part two

    l = len(content)
    i = 0
    j = 1
    sum = content[i] + content[j]
    bon_gaulois = 0
    while j < l:
        if sum < bad_roman:
            j += 1
            sum += content[j]
        elif sum > bad_roman:
            if i == j - 1:
                j += 1
                sum += content[j]
            sum -= content[i]
            i += 1
        if sum == bad_roman:
            bon_gaulois = min(content[i:j+1]) + max(content[i:j+1])
            break

    if do_print:
        print('Mauvais romain 1:', bad_roman)
        print('Bon gaulois 2:', bon_gaulois)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 1124361034
    #   2: 129444555
