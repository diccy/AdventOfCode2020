
def Resolve(do_print = False):

    with open('d02.txt', 'r') as f:
        content = f.read().splitlines()

    bg1 = 0
    bg2 = 0
    for line in content:
        s = line.split(' ')
        numbers = s[0].split('-')
        n_min = int(numbers[0])
        n_max = int(numbers[1])
        letter = s[1][0]
        letter_count = 0
        letter_found = 0
        for i, c in enumerate(s[2]):
            if c == letter:
                letter_count += 1
                if i + 1 == n_min or i + 1 == n_max:
                    letter_found += 1
        if n_min <= letter_count and letter_count <= n_max:
            bg1 += 1
        if letter_found == 1:
            bg2 += 1

    if do_print:
        print('Bons gaulois 1:', bg1)
        print('Bons gaulois 2:', bg2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 458
    #   2: 342
