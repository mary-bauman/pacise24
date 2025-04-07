import sys
for line in sys.stdin:
    line = line.strip().split()
    a = int(line[0])
    b = int(line[1])
    if len(b)==1:
        c = a*b
        length = max(len(c),len(a))
        dash = "-"*(max(len(a),len(b)))
        while(len(str(a))<length):
            a = " " + str(a)
        while(len(str(b))<length):
            b = " " + str(b)
        
        while len(dash)<length:
            dash = " " + str(dash)
        print(a)
        print(b)
        print(dash)
        
