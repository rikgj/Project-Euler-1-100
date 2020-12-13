'''
Let d(n) be defined as the sum of proper divisors of n (numbers less than n which divide evenly into n).
If d(a) = b and d(b) = a, where a ≠ b, then a and b are an amicable pair and each of a and b are called amicable numbers.

For example,
the proper divisors of 220 are 1, 2, 4, 5, 10, 11, 20, 22, 44, 55 and 110; therefore
d(220) = 284.
The proper divisors of 284 are 1, 2, 4, 71 and 142; so
d(284) = 220.

Evaluate the sum of all the amicable numbers under 10000.
'''

from math import sqrt
def sum_of_all_divisors(num):
    '''return the sum of all proper divisors less than n'''
    sum_divs = 0
    divisor = 1
    while divisor <= sqrt(num):
        if(num%divisor == 0):
            sum_divs+=divisor
            if(divisor != num/divisor):
                sum_divs+=num/divisor
        divisor+=1

    # remove itself as a valid divisor
    sum_divs-=num

    return int(sum_divs)


amicables = []
num = 1

# find all amicables under 10 000
while num < 10000:
    # check if amicable
    pot_amicable = sum_of_all_divisors(num)
    # validate number
    if (sum_of_all_divisors(pot_amicable) == num and pot_amicable != num):
        # add to cart if not alreaddy present
        if num not in amicables:
            amicables.append(pot_amicable)
            amicables.append(num)
    num+=1

# Evaluate the sum of all the amicable numbers under 10 000
sum = 0
print(amicables)
for am in amicables:
    sum+=am

print(sum)
