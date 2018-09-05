import sys


# Return the trie built from patterns
# in the form of a dictionary of dictionaries,
# e.g. {0:{'A':1,'T':2},1:{'C':3}}
# where the key of the external dictionary is
# the node ID (integer), and the internal dictionary
# contains all the trie edges outgoing from the corresponding
# node, and the keys are the letters on those edges, and the
# values are the node IDs to which these edges lead.
#
# input: ["ATAGA", "ATC", "GAT"]
# output:
# 0->1:A
# 0->7:G
# 1->2:T
# 2->3:A
# 2->6:C
# 3->4:G
# 4->5:A
# 7->8:A
# 8->9:T


def build_trie(patterns):
    tree = dict()

    # the label for vertex
    count = 0
    tree[0] = {}

    for p in patterns:
        root = 0
        p_count = 0
        for s in p:
            p_count += 1
            if s not in tree[root]:
                count += 1
                tree[root][s] = count
                root = count
                if p_count < len(p):
                    tree[root] = {}
            else:
                root = tree[root][s]

    return tree


if __name__ == '__main__':
    patterns = sys.stdin.read().split()[1:]
    tree = build_trie(patterns)
    for node in tree:
        for c in tree[node]:
            print("{}->{}:{}".format(node, tree[node][c], c))
