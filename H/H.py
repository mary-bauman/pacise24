import sys

i = 1
for ln in sys.stdin:
    d = dict()
    ln = ln.strip().split(", ")
    for edge in ln:
        ed = edge.split()
        if ed[1] not in d:
            d[ed[1]] = []
        d[ed[1]].append(ed[0])
    numPoints = 0
    valid = True
    visited = set()
    for edge in ln:
        ed = edge.split()
        if ed[0] not in d and ed[0] not in visited:
            numPoints += 1
            visited.add(ed[0])
        elif len(d[ed[1]]) > 1:
            valid = False
    if numPoints == 1 and valid:
        print("Case " + str(i) + " is a tree.")
    else:
        print("Case " + str(i) + " is not a tree.")
    i += 1