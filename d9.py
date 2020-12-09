with open("d9.txt", "r") as f:
    content = [int(s) for s in f.read().splitlines()]

bad_roman = 0

# Part one

# This solution totally fails at not using the same number twice,
# and is fucked up if there is 2 or more different entries with the same
# value, erasing all of them when doing dic.pop(nmp).

P = 25
tab = [0] * P
dic = {}

i = 0
for n in content:
    if i >= P:
        sum = None
        j = 0
        while j < P:
            m = tab[j]
            if dic.get(n - m):
                sum = (j, m)
                break
            j += 1
        if sum == None:
            bad_roman = n
            print("Mauvais romain 1:", bad_roman)
            break
        nmp = tab[i % P]
        dic.pop(nmp)
    tab[i % P] = n
    dic[n] = True
    i += 1


# Part two

l = len(content)
i = 0
j = 1
sum = content[i] + content[j]
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
        min = min(content[i:j+1])
        max = max(content[i:j+1])
        print("Bon gaulois 2:", min + max)
        break
