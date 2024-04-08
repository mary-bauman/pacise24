import sys

stamps = [int(i) for i in input().split()]

ln = "STAMP VALUES"
for s in stamps:
    ln += f" {s}"
print(ln + "\n")

stamps.sort()

for line in sys.stdin:
    if line == '\n': break

    n = int(line)
    print(f"AMOUNT {n}")

    if n < stamps[0]:
        print("NO SOLUTION EXISTS\n")
        continue

    if n > stamps[-1]*10:
        print("NO SOLUTION EXISTS\n")
        continue

    dp = [[] for _ in range(n+1)]
    visited = []

    for i in range(len(dp)):
        if i and dp[i] == []: continue
        for s in stamps:
            if i+s > n: continue
            if dp[i+s] != [] and len(dp[i+s]) <= len(dp[i])+1: continue
            dp[i+s] = dp[i] + [s]
            visited.append(i+s)

    ans = dp[-1]
    if ans == []:
        for v in sorted(visited, reverse = True):
            if ans == []:
                ans = dp[v] + [stamps[0]]
            elif n < v+stamps[0] < sum(ans):
                ans = dp[v] + [stamps[0]]

    ln = "STAMPS USED"
    for s in sorted(ans, reverse=True):
        ln += f" {s}"
    print(ln + "\n")
