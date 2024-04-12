import sys

for ln in sys.stdin:
    ln = ln.strip()
    if ln.isdecimal():
        lnInt = int(ln)
        ans = ""
        while lnInt > 0:
            char = lnInt % 26
            if char == 0:
                char = 26
            ans = chr(char + ord('a') - 1) + ans
            lnInt -= (char)
            lnInt //= 26
        print(ans + " " + ln)

    else:
        ans = 0
        ln = ln.lower()
        for c in ln:
            ans = ans * 26 + (ord(c) - ord('a') + 1)
        print(ln + " " +str(ans))