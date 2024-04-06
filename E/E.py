import sys
for line in sys.stdin:
    if line=='\n': break
    s = []
    line = line.strip().split()
    #s.append(line)
    a = int(line[0])
    b = int(line[1])
    s.append(a)
    s.append(b)
    n = max(len(str(a)),len(str(b)))
    s.append("-"*n)
    t = []
    zeros = []
    if len(str(b))==1:
        s.append(a*b)
    else:
        newB = str(b)[::-1]
        for y in newB:
            t.append(str((int(y))*a))
        m = 0
        tts = []
        zeros = 0
        for tti in range(len(t)):
            tt = str(t[tti]) + "0"*tti
            zeros +=tti
            tts.append(tt)
            s.append(t[tti])
            m += int(tt)
        #print("tts")
        #print(tts)
        n = len(max(tts, key=len))
        s.append("-"*n)
        s.append(str(m) + str(" "*int(zeros)))

    spaces = 0
    for line in s:
        if len(str(line))>spaces:
            spaces = len(str(line))
    spaces -=1
    for ss in s:
        #print("ss")
        #print(ss)
        spc = max(0,int(spaces - len(str(ss))))
        #print(spc)
        newSs = " "*spc
        newSs += str(ss)
        print(newSs)


    print("")



