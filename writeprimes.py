import math

limit = 2000
list = [True] * (limit+1)
i = 2
limit_i = math.floor(math.sqrt(limit))
while i <= limit_i:
    if(list[i]):
        n=0
        j = i**2 + i*n
        while j < limit:
            list[j] = False
            n+=1
            j = i**2 + i*n
    i+=1

index = 2

primes = []

while index < limit:
    if(list[index]):
        primes.append(index)
    index+=1


with open('primes.txt', 'w') as f:
    for prime in primes:
        print(prime, file=f)
