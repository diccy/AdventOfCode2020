from collections import deque

def Resolve(do_print = False):

    with open('d19.txt', 'r') as f:
        content = f.read().splitlines()

    rules_dict = {}
    i = 0
    for i, line in enumerate(content):
        if len(line) == 0:
            break
        entries = line.split(':')
        n = int(entries[0])
        if entries[1][1] == '"':
            r = entries[1][2]
        else:
            r = tuple([tuple([int(s) for s in reversed(rs.split(' ')) if len(s) > 0]) for rs in entries[1].split('|')])
        rules_dict[n] = r

    rules = [None] * (max(rules_dict.keys()) + 1)
    for k, v in rules_dict.items():
        rules[k] = v
    rules_dict = {}

    test_line = None
    rid_stack = deque()
    def TestRuleRec(offset):
        if offset == len(test_line):
            return len(rid_stack) == 0
        if len(rid_stack) == 0:
            return False
        rid = rid_stack.pop()
        current_rule = rules[rid]
        if type(current_rule) is tuple:
            for rid_set in current_rule:
                l = len(rid_stack)
                rid_stack.extend(rid_set)
                if TestRuleRec(offset):
                    return True
                while len(rid_stack) > l:
                    rid_stack.pop()
        else:
            if test_line[offset] == current_rule:
                return TestRuleRec(offset + 1)
        rid_stack.append(rid)
        return False

    def TestRule(line, rule):
        nonlocal test_line
        test_line = line
        rid_stack.clear()
        rid_stack.append(rule)
        return TestRuleRec(0)

    # Part 1
    lg1 = sum([1 for line in content[i+1:] if TestRule(line, 0)])

    # Part 2
    # 8: 42 | 42 8
    # 11: 42 31 | 42 11 31
    # reversed like during parsing
    rules[8] = ((42,), (8, 42))
    rules[11] = ((31, 42), (31, 11, 42))
    lg2 = sum([1 for line in content[i+1:] if TestRule(line, 0)])

    if do_print:
        print('Entrees gauloises 1:', lg1)
        print('Entrees gauloises 2:', lg2)


# #############################################################################
if __name__ == '__main__':
    Resolve(True)
    # Results with given input:
    #   1: 220
    #   2: 439
