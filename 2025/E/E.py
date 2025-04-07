#written by Ben Crocker / Byte Me

from sys import stdin

n = input()

j = 1

while True:
    try:
        n = input()
    except EOFError:
        break

    s = input().split("##")

    needed = 0

    for seq in s:
        curr = []
        for i, c in enumerate(seq):
            if i % 3 == 0:
                curr.append([c])
            else:
                curr[-1].append(c)
        needed += len([x for x in curr if '.' in x])

    print(f"Case {j}:", needed)
    j += 1