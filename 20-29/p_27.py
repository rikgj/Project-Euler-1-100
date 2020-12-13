'''
Euler discovered the remarkable quadratic formula:

n2+n+41
It turns out that the formula will produce 40 primes for the consecutive integer values 0≤n≤39.
However, when n=40,402+40+41=40(40+1)+41 is divisible by 41, and certainly when n=41,412+41+41 is clearly divisible by 41.

The incredible formula n2−79n+1601 was discovered, which produces 80 primes for the consecutive values 0≤n≤79.
The product of the coefficients, −79 and 1601, is −126479.

Considering quadratics of the form:

n2+an+b, where |a|<1000 and |b|≤1000

where |n| is the modulus/absolute value of n
e.g. |11|=11 and |−4|=4
Find the product of the coefficients, a and b, for the quadratic expression that produces
the maximum number of primes for consecutive values of n, starting with n=0.
'''
import math
known_primes = [2,3,5,7,11]

# check if a given number is a prime number
def check_if_prime(num):
    # check that num is greater than 1
    if num <= 1:
        return False

    # check if a known prime is a factor
    for prime in known_primes:
        if(num%prime == 0) and num != prime:
            return False

    # brute force
    divisor = 2
    limit = math.sqrt(num)
    while divisor <= limit:
        if(num%divisor == 0) and num != divisor:
            return False
        divisor+=1

    return True


# find the best setup for f(n) = n**2 +a*n +b

a = -999
abwinner = (1,41)
tot_primes = 0

while a < 1000:
    num_of_primes = 0
    b = 2
    while b <= 1000:
        num_of_primes = 0
        n = 0
        stillgood = True
        while stillgood:
            num = n**2 + a*n + b
            if num not in known_primes:
                if check_if_prime(num):
                    # add to list
                    known_primes.append(num)
                    num_of_primes+=1
                else:
                    stillgood = False
            else:
                num_of_primes+=1

            n+=1

        # check if we have a new best ab-pair
        if(num_of_primes > tot_primes):
            tot_primes = num_of_primes
            abwinner = (a, b)
            print(" The AB pair: {}, the amount of primes: {}".format(abwinner, tot_primes))

        b+=1
    a+=1

# print the winner combination and the product of ab
abprod = abwinner[0] * abwinner[1]
print(" The AB pair: {}, the amount of primes: {}, the product of a*b = {}".format(abwinner, tot_primes, abprod))
