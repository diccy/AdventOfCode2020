with open("d13.txt", "r") as f:
    content = f.read().splitlines()

timestamp = int(content[0])
buses = [(int(b), i) for i, b in enumerate(content[1].split(',')) if b != 'x']


# Part 1

min_wait = timestamp
min_bus = -1
for bi in buses:
    wait = bi[0] - (timestamp % bi[0])
    if wait < min_wait:
        min_wait = wait
        min_bus = bi[0]

print("Bus gaulois 1:", min_wait * min_bus)


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

def GCD(a, b):
    return a if b == 0 else GCD(b, a % b)

# Assert coprimes
i = 0
l = len(buses)
coprimes = True
while i < l - 1:
    j = i + 1
    while j < l:
        if GCD(buses[i][0], buses[j][0]) != 1:
            coprimes = False
            print("Entree pas tres gauloise 2:", buses[i][0], "et", buses[j][0], "ne sont pas premiers entre eux!")
            break
        j += 1
    i += 1

if coprimes:

    # d == GCD(a, b), au + bv == d
    def ExtendedEuclidean(a, b):
        d, u, v, d1, u1, v1 = a, 1, 0, b, 0, 1
        while d1 != 0:
            q = d // d1
            d, u, v, d1, u1, v1 = d1, u1, v1, d - (q * d1), u - (q * u1), v - (q * v1)
        return (d, u, v)

    mult = 1
    for bi in buses:
        mult *= bi[0]
    print("mult:", mult)

    x = 0
    for bi in buses:
        n_ = mult // bi[0]
        d, u, v = ExtendedEuclidean2(n_, bi[0])
        x += (bi[0] - bi[1]) * (u % bi[0]) * n_
        print("n:", bi[0],"n_:", n_, "d:", d, (n_ * u) + (bi[0] * v),"u:", u, "v:", v,"e:", (u % bi[0]) * n_)
    x = x % mult

    print("Timestamp gaulois 2:", x)
