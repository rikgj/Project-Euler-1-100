'''
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10.

In general, (nr)=n!r!(n−r)!, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1.

It is not until n=23, that a value exceeds one-million: (2310)=1144066.

How many, not necessarily distinct, values of (nr) for 1≤n≤100, are greater than one-million?
'''

import math
import timeit

def prob53():
    n = 23
    r = 4
    matches = 0
    facts = [0,1,2,3]
    f = 4
    while f <=100:
        facts.append(math.factorial(f))
        f+=1

    while n <= 100:
        r = 4
        while r <= n/2:
            val = facts[n]/(facts[r]*facts[n-r])
            if (val) > 1000000:
                # all values of r to, and including (n - r) will have 1 000 000 or higher val
                matches += n - 2*r + 1
                r+=100
            r+=1
        n+=1

    return matches

reps = 100
execution_time = timeit.timeit(prob53, number=reps)
print(execution_time/reps)
print(prob53())
