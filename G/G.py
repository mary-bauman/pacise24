from sys import stdin

digitMap = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"

def from_base(n, b):
    o = 0
    for i, c in enumerate(reversed(n)):
        idx = digitMap.index(c)
        if idx + 1 > b:
            return None
        else:
            o += idx * (b ** i)
    return o

def main():
    for line in stdin:
        nums = line[:-1].split()
        solved = False
        for b in range(2, 37):
            flag = False
            val1 = from_base(nums[0], b)
            if val1 is None:
                continue
            for b2 in range(2, 37):
                val2 = from_base(nums[1], b2)
                if (val2 is not None) and val1 == val2:
                    flag = True
                    print(f"{nums[0]} (base {b}) = {nums[1]} (base {b2})")
                    break
            if flag:
                solved = True
                break
        if not solved:
            print(f"{nums[0]} is not equal to {nums[1]} in any base 2..36")

main()
