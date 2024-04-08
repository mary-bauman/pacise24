import sys

for idx, ln in enumerate(sys.stdin):
    s = ln.split()
    ans = 0

    i = 0
    for frame in range(10):
        if s[i].isdigit():
            if s[i+1] == '/':
                ans += 10
                if s[i+2] == 'X':
                    ans += 10
                else:
                    ans += int(s[i+2])
            else:
                ans += int(s[i]) + int(s[i+1])

            i += 2
        elif s[i] == 'X':
            ans += 10

            if s[i+1] == 'X':
                ans += 10

                if s[i+2] == 'X':
                    ans += 10
                else:
                    ans += int(s[i+2])
            else:
                if s[i+2] == '/':
                    ans += 10
                else:
                    ans += int(s[i+1]) + int(s[i+2])

            i += 1

    print(f"Game {idx+1}: {ans}")
