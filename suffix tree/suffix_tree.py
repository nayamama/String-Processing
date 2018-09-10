# python3
# the suffix tree initiation code is writen by Ben Langmead
#

import sys


class SuffixTree(object):
    class Node(object):
        def __init__(self, lab):
            self.lab = lab  # label on path leading to this node
            self.out = {}  # outgoing edges; maps characters to nodes

        def __str__(self):
            return self.lab

    def __init__(self, s):
        """ Make suffix tree, without suffix links, from s in quadratic time and linear space """
        self.root = self.Node(None)
        self.root.out[s[0]] = self.Node(s)  # trie for just longest suf
        # add the rest of the suffixes, from longest to shortest
        for i in range(1, len(s)):
            # start at root; we’ll walk down as far as we can go
            cur = self.root
            j = i
            while j < len(s):
                if s[j] in cur.out:
                    child = cur.out[s[j]]
                    lab = child.lab
                    # Walk along edge until we exhaust edge label or until we mismatch
                    k = j + 1
                    while k - j < len(lab) and s[k] == lab[k - j]:
                        k += 1
                    if k - j == len(lab):
                        cur = child  # we exhausted the edge
                        j = k
                    else:
                        # we fell off in middle of edge
                        cExist, cNew = lab[k - j], s[k]
                        # create “mid”: new node bisecting edge
                        mid = self.Node(lab[:k - j])
                        mid.out[cNew] = self.Node(s[k:])
                        # original child becomes mid’s child
                        mid.out[cExist] = child
                        # original child’s label is curtailed
                        child.lab = lab[k - j:]
                        # mid becomes new child of original parent
                        cur.out[s[j]] = mid
                else:
                    # Fell off tree at a node: make new edge hanging off it
                    cur.out[s[j]] = self.Node(s[j:])

    def print_edges(self, node):
        for child in node.out:
            print(node.out[child].lab)
            self.print_edges(node.out[child])


if __name__ == '__main__':

    # text = sys.stdin.readline().strip()
    text = "ATAAATG$"
    result = SuffixTree(text)
    result.print_edges(result.root)
