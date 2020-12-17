import numpy as np

def Resolve(do_print = False):

    with open('d16.txt', 'r') as f:
        content = f.read().splitlines()

    names = []
    fields = []
    content_offset = 0
    for i, line in enumerate(content):
        if len(line) > 0:
            s = line.split(': ')
            names.append(s[0])
            fields_pair = [int(v) for pair in s[1].split(' or ') for v in pair.split('-')]
            fields.append(fields_pair)
        else:
            content_offset = i
            break
    
    fields_count = len(fields)
    
    my_ticket = [int(s) for s in content[content_offset+2].split(',')]

    tickets = []
    for line in content[content_offset+5:]:
        tickets.append([int(s) for s in line.split(',')])

    valid_tickets = []
    errors_sum = 0
    for ticket in tickets:
        is_ticket_valid = True
        for value in ticket:
            is_value_valid = False
            for field in fields:
                if (field[0] <= value and value <= field[1]) or (field[2] <= value and value <= field[3]):
                    is_value_valid = True
                    break
            if not is_value_valid:
                errors_sum += value
                is_ticket_valid = False
                break
        if is_ticket_valid:
            valid_tickets.append(ticket)
    
    a = np.ones((fields_count, fields_count), dtype=np.uint8)
    for ticket in valid_tickets:
        for i, value in enumerate(ticket):
            for j, field in enumerate(fields):
                if not ((field[0] <= value and value <= field[1]) or (field[2] <= value and value <= field[3])):
                    a[i,j] = 0

    more_than_one = 1
    while more_than_one > 0:
        more_than_one = 0
        for r, row in enumerate(a):
            nz = np.flatnonzero(row)
            if len(nz) == 1:
                a[:,nz[0]] = 0
                a[r,nz[0]] = 1
            else:
                more_than_one += 1
        for c in range(a.shape[1]):
            nz = np.flatnonzero(a[:,c])
            if len(nz) == 1:
                a[nz[0],:] = 0
                a[nz[0],c] = 1
            else:
                more_than_one += 1

    departure_product = 1
    for c in range(a.shape[1]):
        nz = np.flatnonzero(a[:,c])
        if len(nz) > 0:
            i = nz[0]
            if names[c].startswith('departure'):
                departure_product *= my_ticket[i]

    if do_print:
        print("Somme gauloise 1:", errors_sum)
        print("Produit gaulois 2:", departure_product)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 19093
    #   2: 5311123569883
