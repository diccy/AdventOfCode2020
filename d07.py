
def Resolve(do_print = False):

    with open('d07.txt', 'r') as f:
        content = [tuple(line.split(' bags contain ')) for line in f.read().splitlines()]

    class Bag:
        def __init__(self):
            self.parents = []
            self.children = []
            self.visited = False

    bags = {}
    for desc in content:
        current_hname = hash(desc[0])
        current_bag = bags.get(current_hname)
        if current_bag == None:
            current_bag = Bag()
            bags[current_hname] = current_bag
        for child_desc in desc[1].split(', '):
            if child_desc[0] == 'n':
                break  # 'no other bags.'
            child_count = int(child_desc[0])
            child_hname = hash(child_desc[2:child_desc.find(' bag', 2)])
            child_bag = bags.get(child_hname)
            if child_bag == None:
                child_bag = Bag()
                bags[child_hname] = child_bag
            child_bag.parents.append(current_bag)
            current_bag.children.append((child_bag, child_count))

    def GetParents(bag):
        bag.visited = True
        total = 1
        for parent_bag in bag.parents:
            if not parent_bag.visited:
                total += GetParents(parent_bag)
        return total

    def GetChildren(bag):
        total = 1
        for child_bag, n in bag.children:
            total += GetChildren(child_bag) * n
        return total

    if do_print:
        h_shiny_gold = hash('shiny gold')
        print('Gaulois parents:', GetParents(bags.get(h_shiny_gold)) - 1)
        print('Gaulois enfants:', GetChildren(bags.get(h_shiny_gold)) - 1)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 252
    #   2: 35487
