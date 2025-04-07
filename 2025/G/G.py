#written by Byte Me

while n := int(input()):
    names = [input() for _ in range(n)]
    names.sort()
    edge = names[(n//2)-1:n//2+1]

    ans = ""
    min_len = min(map(len, edge))
    for i in range(min_len):
        if edge[0][i] != edge[1][i]:
            ans += chr(ord(edge[0][i])+1)
            break
        ans += edge[0][i]

    print(ans)
