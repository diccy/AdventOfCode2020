with open("d3.txt", "r") as f:
    content = f.read().splitlines()

def TreeCount(map, w, h, stepx, stepy):
    tree_count = 0
    i = 0
    for j in range(0, h, stepy):
        if map[j][i] == '#':
            tree_count += 1
        i = (i + stepx) % w
    return tree_count

w = len(content[0])
h = len(content)
tree_count11 = TreeCount(content, w, h, 1, 1)
tree_count31 = TreeCount(content, w, h, 3, 1)
tree_count51 = TreeCount(content, w, h, 5, 1)
tree_count71 = TreeCount(content, w, h, 7, 1)
tree_count12 = TreeCount(content, w, h, 1, 2)
print("Result: ", tree_count11 * tree_count31 * tree_count51 * tree_count71 * tree_count12)
