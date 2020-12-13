'''
By listing the first six prime numbers: 2, 3, 5, 7, 11, and 13, we can see that the 6th prime is 13.

What is the 10 001st prime number?

'''

import math
# this needs to be high in order to find enough primes
limit = 1000000
# create a list with limit+1 entries all set to True
list = [True] * (limit+1)
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

primes = [1]
index = 2
while index <= math.ceil(limit/2):
    if(list[index]):
        primes.append(index)
    index+=1

# prints out the 10001th prime if it is in the list
if(len(primes) >= 10001):
    print(primes[10001])
else:
    print("You need to increase the limit")
