import sys

for ln in sys.stdin:
    ln = ln.split()
    n1 = ln[0]
    n2 = ln[1]
    if n1[-1].isdigit():
        minN1 = int(n1[-1]) + 1
    else:
        minN1 = ord(n1[-1]) - ord('A') + 11
    if n2[-1].isdigit():
        minN2 = int(n2[-1]) + 1
    else:
        minN2 = ord(n2[-1]) - ord('A') + 11
    maxMin = max(minN1, minN2)
    bases1 = [0] * (37 - maxMin)
    bases2 = [0] * (37 - maxMin)
    for i in range(maxMin, 37):
        base1 = ""
        for j in range(len(n1)):
            if 