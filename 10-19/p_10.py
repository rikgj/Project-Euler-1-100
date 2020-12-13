'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''

# find all the primes below 2 000 000 using solution from problem 7

import math
# limit set to two millions
limit = 2000000
# create a list with limit entries all set to True
list = [True] * (limit)
i = 2
limit_i = math.floor(math.sqrt(limit))
while i <= limit_i:
    # check if number is prime
    if(list[i]):
        n=0
        i2 = i**2
        j = i2
        while j < limit:
            # set non-prime index numeber to false
            list[j] = False
            n+=1
            j = i2 + i*n
    i+=1

primes = []
index = 2
while index < limit:
    if(list[index]):
        primes.append(index)
    index+=1

# sum the primes
sum = 0
for prime in primes:
    sum+=prime

print(sum)
