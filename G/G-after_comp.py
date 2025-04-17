import sys

for line in sys.stdin:
    line = line.strip().split()
    one = line[0]
    two = line[1]
    i = 2
    minJ = 2
    ans = (0,0)
    
    for char in one:
        if char.isalpha():
            i = max(ord(char)-54,i)
        else:
            i = max(int(char)+1,i) 
    
    for char in two:
        if char.isalpha():
            minJ = max(ord(char)-54,minJ)
        else:
            minJ = max(int(char)+1,minJ)
    
    while i < 37 and ans == (0,0):
        newI = 0
        cur = 1
        for n in range(len(one)-1,-1,-1):
            if one[n].isalpha():
                newI += (ord(one[n])-55) * cur
            else:
                newI += int(one[n]) * cur
            cur*=i
        
        j = minJ
        while j < 37:
            newNum = 0
            cur = 1
            for n in range(len(two)-1,-1,-1):
                if two[n].isalpha():
                    newNum += (ord(two[n])-55)*cur
                else:
                    newNum += int(two[n])*cur
                cur*=j
        
            if newNum == newI:
                if ans == (0,0):
                    ans = (i,j)
                       
            j+=1
        i+=1
    if ans == (0,0):
        print(f"{one} is not equal to {two} in any base 2..36")
    else:
        print(f"{one} (base {ans[0]}) = {two} (base {ans[1]})")
