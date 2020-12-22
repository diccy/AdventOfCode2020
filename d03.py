
def Resolve(do_print = False):

    with open('d03.txt', 'r') as f:
        content = f.read().splitlines()

    w = len(content[0])
    h = len(content)

    def TreeCount(stepx, stepy):
        tree_count = 0
        i = 0
        for j in range(0, h, stepy):
            if content[j][i] == '#':
                tree_count += 1
            i = (i + stepx) % w
        return tree_count

    tree_count11 = TreeCount(1, 1)
    tree_count31 = TreeCount(3, 1)
    tree_count51 = TreeCount(5, 1)
    tree_count71 = TreeCount(7, 1)
    tree_count12 = TreeCount(1, 2)

    if do_print:
        print('Arbres gaulois 1:', tree_count31)
        print('Arbres gaulois 2:', tree_count11 * tree_count31 * tree_count51 * tree_count71 * tree_count12)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 247
    #   2: 2983070376
