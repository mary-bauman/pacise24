#written by Byte Me

while (n := int(input())) != -1:
    # scouts, all
    ans = [0, 1]
    for i in range(n):
        scouts = ans[1]
        all = ans[0] + scouts + 1
        ans = [scouts, all]

    print(ans[0], ans[1])

