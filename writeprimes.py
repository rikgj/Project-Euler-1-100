import math

limit = 10**8
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


with open('primes.txt', 'w') as f:
    while index < limit:
        if(list[index]):
            print(index, file=f)
        index+=1
