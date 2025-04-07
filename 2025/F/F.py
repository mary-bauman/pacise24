#by Mary Bauman / Byte Me

from math import inf
go = True
while go:
    try:
        nums = [int(a) for a in input().split()][:-1]
        n = len(nums)
        if n==0: print(0)
        elif n==1: print(nums[0])
        else:
            negsZ = sum([1 for n in nums if n<=0])        
            prod = 1
            for x in nums: prod *= x
            if negsZ==0:
                print(prod)
            else:
                best = nums[0]
                for start in range(n):
                    cur = nums[start]
                    best = max(best, cur)
                    for end in range(start + 1, n):
                        cur *= nums[end]
                        best = max(best, cur)
                print(best)


    except EOFError:
       go = False