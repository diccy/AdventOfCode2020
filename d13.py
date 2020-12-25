
def Resolve(do_print = False):

    with open('d13.txt', 'r') as f:
        content = f.read().splitlines()

    timestamp = int(content[0])
    buses = [(int(b), i) for i, b in enumerate(content[1].split(',')) if b != 'x']


    # Part 1

    min_wait = timestamp
    min_bus = -1
    for bus, _ in buses:
        wait = bus - (timestamp % bus)
        if wait < min_wait:
            min_wait = wait
            min_bus = bus

    bg1 = min_wait * min_bus


    # Part 2

    # https://fr.wikipedia.org/wiki/Congruence_linéaire
    # https://fr.wikipedia.org/wiki/Inverse_modulaire
    # https://fr.wikipedia.org/wiki/Algorithme_d%27Euclide_%C3%A9tendu
    # https://fr.wikipedia.org/wiki/Th%C3%A9or%C3%A8me_des_restes_chinois#Algorithme

    # Solution x du systeme:
    # x == (buses[0][0] - buses[0][1]) (mod buses[0][0])
    # x == (buses[1][0] - buses[1][1]) (mod buses[1][0])
    # ...
    # x == (buses[n][0] - buses[n][1]) (mod buses[n][0])

    # Assert coprimes

    coprimes = True

    #def GCD(a, b):
    #    return a if b == 0 else GCD(b, a % b)

    #i = 0
    #l = len(buses)
    #while i < l - 1:
    #    j = i + 1
    #    while j < l:
    #        if GCD(buses[i][0], buses[j][0]) != 1:
    #            coprimes = False
    #            tg2 = 'Error'
    #            if do_print:
    #                print('Entree pas tres gauloise 2:', buses[i][0], 'et', buses[j][0], 'ne sont pas premiers entre eux!')
    #            break
    #        j += 1
    #    i += 1

    if coprimes:

        # d == GCD(a, b), au + bv == d
        def ExtendedEuclidean(a, b):
            d, u, v, d1, u1, v1 = a, 1, 0, b, 0, 1
            while d1 != 0:
                q = d // d1
                d, u, v, d1, u1, v1 = d1, u1, v1, d - (q * d1), u - (q * u1), v - (q * v1)
            return (d, u, v)

        mult = 1
        for bus, _ in buses:
            mult *= bus

        x = 0
        for bus, i in buses:
            n = mult // bus
            _, u, _ = ExtendedEuclidean(n, bus)
            x += (bus - i) * (u % bus) * n
        tg2 = x % mult


    if do_print:
        print('Bus gaulois 1:', bg1)
        print('Timestamp gaulois 2:', tg2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 4938
    #   2: 230903629977901
