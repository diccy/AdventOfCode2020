
def Resolve(do_print=False):

    with open('d24.txt', 'r') as f:
        content = f.read().splitlines()

    # Axial scheme
    #                e        ne       se       w        nw       sw
    NEIGHBOURS = (( 1, 0), ( 1,-1), ( 0, 1), (-1, 0), ( 0,-1), (-1, 1))
    AddTuples = lambda a, b: (a[0] + b[0], a[1] + b[1])

    black_tiles = {}
    dir_offset = 0
    for line in content:
        tile_pos = (0, 0)
        for c in line:
            if c == 'n':
                dir_offset = 1
            elif c == 's':
                dir_offset = 2
            else:
                if c == 'w':
                    dir_offset += 3
                tile_pos = AddTuples(tile_pos, NEIGHBOURS[dir_offset])
                dir_offset = 0
        if tile_pos in black_tiles:
            black_tiles.pop(tile_pos)
        else:
            black_tiles[tile_pos] = True

    black_tiles_count1 = len(black_tiles)

    for _ in range(100):
        white_tiles = {}
        for k in black_tiles.keys():
            for n_dir in NEIGHBOURS:
                n = AddTuples(k, n_dir)
                if not n in black_tiles:
                    white_tiles[n] = white_tiles.get(n, 0) + 1

        black_tiles_to_white = []
        for k in black_tiles.keys():
            n_count = 0
            for n_dir in NEIGHBOURS:
                n = AddTuples(k, n_dir)
                if n in black_tiles:
                    n_count += 1
            if n_count == 0 or n_count > 2:
                black_tiles_to_white.append(k)
        for k in black_tiles_to_white:
            black_tiles.pop(k)

        for k, n_count in white_tiles.items():
            if n_count == 2:
                black_tiles[k] = True

    black_tiles_count2 = len(black_tiles)

    if do_print:
        print("Tuiles gauloises 1:", black_tiles_count1)
        print("Tuiles gauloises 2:", black_tiles_count2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 400
    #   2: 3768
