import sys

# input:
# text: AATCGGGTTCAATCGGGGT, patterns: ["ATCG", "GGGT"]
# output:
# 1 4 11 15


def build_trie(patterns):
    tree = dict()
    tree[0] = {}
    idx = 1

    for p in patterns:
        cur = tree[0]
        for s in p:
            if s in cur:
                cur = tree[cur[s]]
            else:
                cur[s] = idx
                tree[idx] = {}
                cur = tree[idx]
                idx += 1
    return tree


def prefix_trie_matching(text, trie):
    idx = 0
    symbol = text[idx]
    cur = trie[0]

    while True:
        if not cur:
            return True
        elif symbol in cur:
            cur = trie[cur[symbol]]
            idx += 1
            if idx < len(text):
                symbol = text[idx]
            else:
                symbol = "$"
        else:
            return False


def solve(text, n, patterns):
    result = []
    trie = build_trie(patterns)

    for i in range(len(text)):
        if prefix_trie_matching(text[i:], trie):
            result.append(i)

    return sorted(result)


text = sys.stdin.readline().strip()
n = int(sys.stdin.readline().strip())
patterns = []
for i in range(n):
    patterns += [sys.stdin.readline().strip()]

ans = solve(text, n, patterns)

sys.stdout.write(' '.join(map(str, ans)) + '\n')
