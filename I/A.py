import sys
count = 0
a = ""
b = ""
c = ""
for line in sys.stdin:
    if count==3:
        count = 0
    if count==0:
        a = line
        count+=1
    elif count==1:
        b = line
        count+=1
    elif count==2:
        c = line
        count+=1
    
        numbers = []
        
        num = []
        i = 0
        while i <= 22:
            if a[i:i+3]== " _ " and b[i:i+3]== "| |" and c[i:i+3]== "|_|":
                num.append(0)
                i+=2
            elif a[i:i+3]=="   " and b[i:i+3]=="  |" and b[i:i+3]==c[i:i+3]:
                num.append(1)
                i+=2
            elif a[i:i+3]== " _ " and b[i:i+3]== " _|" and c[i:i+3]== "|_ ":
                num.append(2)
                i+=2
            elif a[i:i+3]== " _ " and b[i:i+3]== " _|" and c[i:i+3]== " _|":
                num.append(3)
                i+=2
            elif a[i:i+3]== "   " and b[i:i+3]== "|_|" and c[i:i+3]== "  |":
                num.append(4)
                i+=2
            elif a[i:i+3]== " _ " and b[i:i+3]== "|_ " and c[i:i+3]== " _|":
                num.append(5)
                i+=2
            elif a[i:i+3]== " _ " and b[i:i+3]== "|_ " and c[i:i+3]== "|_|":
                num.append(6)
                i+=2
            elif a[i:i+3]== " _ " and b[i:i+3]== "  |" and c[i:i+3]== "  |":
                num.append(7)
                i+=2
            elif a[i:i+3]==  " _ " and b[i:i+3]== "|_|" and c[i:i+3]== "|_|":
                num.append(8)
                i+=2
            elif a[i:i+3]== " _ " and b[i:i+3]== "|_|" and c[i:i+3]== " _|":
                num.append(9)
                i+=2
            
            # if a[i:i+3]== and b[i:i+3]== and c[i:i+3]== :
            #     num.append()
            #     i+=2
            # if a[i:i+3]== and b[i:i+3]== and c[i:i+3]== :
            #     num.append()
            #     i+=2

            i+=1

        numbers = []
        for n in num:
            numbers.append(n)
        #numbers = [4,9,7,3,6,0,8]
        for n in range(1,len(numbers),2):
            new = str(numbers[n]*2)
            newI = 0
            for char in new:
                newI += int(char)
            # print("newI")
            # print(newI)
            numbers[n]=newI

        #print(numbers)
        valid = "INVALID"
        if sum(numbers) % 10 == 0:
            valid = "VALID"
        if len(numbers)!=7:
            valid = "INVALID"

        sn = ""
        for n in num:
            sn+=str(n)
        s = sn + " " + valid
        print(s)
