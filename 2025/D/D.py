#written by Byte Me

import sys

lines = sys.stdin.readlines()

for i in range(1,len(lines),2):
    sym, pairs = [l.split() for l in lines[i-1:i+1]]
    order = {x: [] for x in sym }

    for j in range(0, len(pairs),2):
        order[pairs[j+1]].append(pairs[j])

    # print(order)

    stk = [x for x in sym if not order[x]]
    ans = []
    while stk:
        cur = stk.pop()
        poss = [x for x in sym if x not in cur]

        if not poss:
            ans.append(cur)
            continue

        stk += [cur+x for x in poss if len(order[x]) <= len(cur) and not [z for z in order[x] if z not in cur]]

    for a in sorted(ans):
        print(a)
    print()
