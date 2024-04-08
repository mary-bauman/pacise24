from sys import stdin

def pad(s, l):
    p = l - len(str(s))
    print(f"{' '*p}{s}")

def hr(l, p):
    return pad('-' * max(*[len(str(s)) for s in l]), p)

def main():
    for line in stdin:
        nums = [int(x) for x in line[:-1].split()]
        prod = nums[0] * nums[1]
        padding = len(str(prod))
        pad(nums[0], padding)
        pad(nums[1], padding)
        hr(nums, padding)
        if len(str(nums[1])) != 1:
            guys = [str(nums[0] * int(d)) + (' ' * i) for i, d in enumerate(reversed(str(nums[1])))]
            for guy in guys:
                pad(guy, padding)
            pad("-" * len(str(prod)), padding)
            # hr(guys, padding)
        print(prod)   
        print()     
    
main()
