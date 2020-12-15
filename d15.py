
def Resolve(do_print = False):

    with open('d15.txt', 'r') as f:
        content = [int(s) for s in f.read().split(',')]

    def Part(part, turns):
        spoken = [0] * turns
        for t, n in enumerate(content):
            spoken[n] = t + 1

        next = 0
        for turn in range(len(content) + 1, turns):
            t = spoken[next]
            spoken[next] = turn
            next = turn - t if t > 0 else 0

        print(f'Reponse gauloise {part}: {next}')

    Part(1, 2020)
    Part(2, 30000000)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 1280
    #   2: 651639
