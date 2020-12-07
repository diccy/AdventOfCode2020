with open("d7.txt", "r") as f:
    content = f.read().splitlines()

class Bag:
    def __init__(self, name):
        self.name = name
        self.parents = {} # key:name, value:bag
        self.children = {} # key:name, value:(bag, count)
        self.visited = False

bags = {} # key:name, value:bag
for line in content:
    line_length = len(line)
    bag_name_end = line.find(" bags", 0, line_length)
    current_bag_name = line[:bag_name_end]
    current_bag = bags.get(current_bag_name)
    if current_bag == None:
        current_bag = Bag(current_bag_name)
        bags[current_bag_name] = current_bag
    child_entry_start = bag_name_end + 14 # add " bags contain " length
    while True:
        child_entry_end = line.find(", ", child_entry_start, line_length)
        child_entry = line[child_entry_start:child_entry_end]
        if child_entry[0] == 'n':
            break # "no other bags."
        child_entry_length = len(child_entry)
        child_count_end = child_entry.find(" ", 0, child_entry_length)
        child_count = int(child_entry[:child_count_end])
        child_count_end += 1
        child_bag_name_end = child_entry.find(" bag", child_count_end, child_entry_length)
        child_bag_name = child_entry[child_count_end:child_bag_name_end]
        child_bag = bags.get(child_bag_name)
        if child_bag == None:
            child_bag = Bag(child_bag_name)
            bags[child_bag_name] = child_bag
        child_bag.parents[current_bag_name] = current_bag
        current_bag.children[child_bag_name] = (child_bag, child_count)
        if child_entry_end == -1:
            break
        child_entry_start = child_entry_end + 2

def GetParents(bag):
    bag.visited = True
    total = 1
    for parent_bag in bag.parents.values():
        if not parent_bag.visited:
            total += GetParents(parent_bag)
    return total

print("Gaulois parents:", GetParents(bags.get("shiny gold")) - 1)

def GetChildren(bag):
    total = 1
    for child_bag, n in bag.children.values():
        total += GetChildren(child_bag) * n
    return total

print("Gaulois enfants:", GetChildren(bags.get("shiny gold")) - 1)
