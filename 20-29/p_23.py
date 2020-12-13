'''
A perfect number is a number for which the sum of its proper divisors is exactly equal to the number.
For example, the sum of the proper divisors of 28 would be 1 + 2 + 4 + 7 + 14 = 28, which means that 28 is a perfect number.

A number n is called deficient if the sum of its proper divisors is less than n and it is called abundant if this sum exceeds n.

As 12 is the smallest abundant number, 1 + 2 + 3 + 4 + 6 = 16, the smallest number that can be written as the sum of two abundant numbers is 24.
By mathematical analysis, it can be shown that all integers greater than 28123 can be written as the sum of two abundant numbers.
However, this upper limit cannot be reduced any further by analysis even though it is known that the greatest number that cannot be expressed
as the sum of two abundant numbers is less than this limit.

Find the sum of all the positive integers which cannot be written as the sum of two abundant numbers.
'''

import math

def sum_of_all_divisors(num):
    '''return the sum of all proper divisors less than n'''
    sum_divs = 0
    divisor = 1
    while divisor <= math.sqrt(num):
        if(num%divisor == 0):
            sum_divs+=divisor
            if(divisor != num/divisor):
                sum_divs+=num/divisor
        divisor+=1

    # remove itself as a valid divisor
    sum_divs-=num
    return int(sum_divs)


max_limit = 28123
numbers = [True] * (max_limit)
abundant = []
num = 12

# find all the abundant
while num < max_limit:
    sum = sum_of_all_divisors(num)
    if num < sum:
        abundant.append(num)

    num+=1

# remove all numbers which can be written as the sum of two abundant numbers
limit = len(abundant)
i = 0
while i < limit:
    k = i
    while k < limit:
        sum = abundant[i] + abundant[k]
        if(sum < max_limit):
            numbers[sum] = False
        k+=1
    i+=1


# present the numbers
sum = 0
limit = len(numbers)
index = 0
while index < limit:
    if(numbers[index]):
        sum+=index
    index+=1

print(sum)
