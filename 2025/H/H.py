#written by Byte Me

from sys import stdin

n = input()

for l in stdin:
    line = l.strip()
    if line == "":
        continue
    stack1 = []
    flag = False
    for c in line:
        if c == "{":
            stack1.append('{')
        elif c == "<":
            stack1.append('<')
        elif c == "}" and stack1.pop(-1) != '{':
            flag = True
            break
        elif c == ">" and stack1.pop(-1) != '<':
            flag = True
            break
    if flag or len(stack1) != 0:
        print("Invalid")
    else:
        print("Valid")