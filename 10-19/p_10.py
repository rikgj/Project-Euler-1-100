'''
The sum of the primes below 10 is 2 + 3 + 5 + 7 = 17.

Find the sum of all the primes below two million.
'''
from math import floor, sqrt
# limit set to two millions
limit = 2000000
# create a list with limit entries all set to True
boolPrime = [True] * (limit)
i = 2
limit_i = floor(sqrt(limit))
while i <= limit_i:
    # check if number is prime
    if(boolPrime[i]):
        n=0
        i2 = i**2
        j = i2
        while j < limit:
            # set non-prime index numeber to false
            boolPrime[j] = False
            n+=1
            j = i2 + i*n
    i+=1

# print the sum of the primes (excluding 1)
primes = sum([i for i,val in enumerate(boolPrime) if val])-1
print(primes)
