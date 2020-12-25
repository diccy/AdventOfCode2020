
def Resolve(do_print = False):

    with open('d05.txt', 'r') as f:
        content = f.read().splitlines()

    lowest = 128 * 8
    highest = 0
    occupied_seats_sum = 0
    for line in content:
        seat_id = 0
        for i in range(0, 7):
            if line[i] == 'B':
                seat_id = seat_id + (1 << (9 - i))
        for i in range(7, 10):
            if line[i] == 'R':
                seat_id = seat_id + (1 << (9 - i))
        occupied_seats_sum += seat_id
        if seat_id < lowest: lowest = seat_id
        if seat_id > highest: highest = seat_id

    overall_sum = ((highest * (highest + 1)) - (lowest * (lowest - 1))) // 2
    seat = overall_sum - occupied_seats_sum

    if do_print:
        print('Plus grand id gaulois 1:', highest)
        print('Siege gaulois 2:', seat)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 890
    #   2: 651
