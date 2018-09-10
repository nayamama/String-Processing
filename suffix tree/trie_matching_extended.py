# python3

# input: "ACATA", ["AT", "A", "AG"]
# output: [0, 2, 4]

import sys


def build_trie(patterns):
    """
    build a trie from all patterns and append a "$" as a stop sign for each pattern
    """
    tree = dict()
    tree[0] = {}
    idx = 1

    for pattern in patterns:
        cur = tree[0]
        for char in pattern:
            if char in cur:
                cur = tree[cur[char]]
            else:
                cur[char] = idx
                tree[idx] = {}
                cur = tree[idx]
                idx += 1
        cur["$"] = None
    # print(tree)
    return tree


def prefix_trie_matching(text, trie, external_idx):
    idx = 0
    symbol = text[idx]
    cur = trie[0]
    res = -1

    while True:
        if not cur or "$" in cur:
            return res
        if symbol in cur:
            cur = trie[cur[symbol]]
            res = external_idx
            idx += 1
            if idx < len(text):
                symbol = text[idx]
            elif "$" in cur:
                return res
            else:
                symbol = "*"
                res = -1
        else:
            return res if '$' in cur else -1


def solve(text, n, patterns):
    result = set()
    trie = build_trie(patterns)
    for i in range(len(text)):
        idx = prefix_trie_matching(text[i:], trie, i)
        if idx != -1:
            result.add(idx)

    return sorted(list(result))


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
