def add(*nums):
    sum  =0
    for n in nums:
        sum = sum+n
    return sum
print(add(2,3,5,10,20))