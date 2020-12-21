import numpy as np

def Resolve(do_print = False):

    with open('d21.txt', 'r') as f:
        content = f.read().splitlines()

    ingr_dict = {}
    allerg_dict = {}
    for food in content:
        desc = food.split(' (contains ')
        ingrs = desc[0].split(' ')
        allergs = desc[1][:-1].split(', ')
        for ing in ingrs:
            ingr_dict[ing] = ingr_dict.get(ing, 0) + 1
        for al in allergs:
            if not al in allerg_dict:
                allerg_dict[al] = set(ingrs)
            else:
                allerg_dict[al] = allerg_dict[al] & set(ingrs)

    ingr_list = [k for k in ingr_dict.keys()]
    allerg_list = [k for k in allerg_dict.keys()]
    la = len(allerg_list)
    li = len(ingr_list)
    a = np.zeros((la, li), dtype=np.uint8)
    for i, ingrs in enumerate(allerg_dict.values()):
        for ingr in ingrs:
            j = ingr_list.index(ingr)
            a[i,j] = 1

    more_than_one = True
    while more_than_one:
        more_than_one = False
        for r, row in enumerate(a):
            nz = np.flatnonzero(row)
            l = len(nz)
            if l == 1:
                a[:, nz[0]] = 0
                a[r, nz[0]] = 1
            else:
                more_than_one = True

    for i in range(la):
        nz = np.flatnonzero(a[i])
        if len(nz) == 1:
            allerg_dict[allerg_list[i]] = ingr_list[nz[0]]

    safe_count = 0
    for i, ingr in enumerate(ingr_list):
        if np.sum(a[:, i]) == 0:
            safe_count += ingr_dict[ingr]

    dangerous = []
    sorted_allerg_list = sorted(allerg_list)
    for allerg in sorted_allerg_list:
        dangerous.append(allerg_dict[allerg])
    dangerous_str = ','.join(dangerous)

    if do_print:
        print("Somme gauloise 1:", safe_count)
        print("Ingredients romains 2:", dangerous_str)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 2659
    #   2: rcqb,cltx,nrl,qjvvcvz,tsqpn,xhnk,tfqsb,zqzmzl
