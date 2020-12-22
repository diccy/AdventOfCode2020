from collections import deque

def Resolve(do_print=False):

    with open('d22.txt', 'r') as f:
        content = f.read().split('Player ')[1:]

    player_cards = [[int(c) for c in deck.split('\n')[1:-1] if len(c) > 0] for deck in content]

    def CountScore(p):
        return sum([c * (i+1) for i, c in enumerate(reversed(p))])

    # Part1
    p1, p2 = deque(player_cards[0]), deque(player_cards[1])
    while len(p1) > 0 and len(p2) > 0:
        c1, c2 = p1.popleft(), p2.popleft()
        if c1 > c2:
            p1.append(c1)
            p1.append(c2)
        else:
            p2.append(c2)
            p2.append(c1)

    score1 = CountScore(p1) if len(p1) > 0 else CountScore(p2)

    # Part2
    def Bagarre(p1, p2, n=0):
        games_dict = {}
        while len(p1) > 0 and len(p2) > 0:
            # For a reason, checking only one hand is WAY faster, and yields to same results
            # Maybe, if one hand come back once, it announces the two hands will come back
            # in future draws. So checking one hand saves great amount of time.
            # (2800ms to 249ms)
            # Don't know if it is mathematically correct.
            #h = hash((tuple(p1), tuple(p2)))
            h = hash(tuple(p1))
            if h in games_dict:
                break
            games_dict[h] = True
            c1, c2 = p1.popleft(), p2.popleft()
            p1win = False
            if c1 <= len(p1) and c2 <= len(p2):
                p1win = Bagarre(deque([p1[i] for i in range(c1)]), deque([p2[i] for i in range(c2)]), 1)
            else:
                p1win = c1 > c2
            if p1win:
                p1.append(c1)
                p1.append(c2)
            else:
                p2.append(c2)
                p2.append(c1)
        return len(p1) > 0 if n > 0 else (len(p1) > 0, p1, p2)

    p1win, p1, p2 = Bagarre(deque(player_cards[0]), deque(player_cards[1]))
    score2 = CountScore(p1) if p1win else CountScore(p2)

    if do_print:
        print("Score gaulois 1:", score1)
        print("Score gaulois 2:", score2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 34324
    #   2: 33259
