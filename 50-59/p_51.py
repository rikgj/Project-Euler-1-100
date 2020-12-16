'''
By replacing the 1st digit of the 2-digit number *3,
it turns out that six of the nine possible values: 13, 23, 43, 53, 73, and 83, are all prime.

By replacing the 3rd and 4th digits of 56**3 with the same digit,
this 5-digit number is the first example having seven primes among the ten generated numbers,
yielding the family: 56003, 56113, 56333, 56443, 56663, 56773, and 56993. Consequently 56003,
 being the first member of this family, is the smallest prime with this property.

Find the smallest prime which,
by replacing part of the number (not necessarily adjacent digits) with the same digit, is part of an eight prime value family.
'''
import time

start = time.time()
from itertools import permutations
from collections import Counter

def masking(prime,perm_i):
    # mask if the masked digits are equal else dump in -1
    a = prime[perm_i[0]]
    for i in perm_i:
        if a != prime[i]:
            # dump number in -1
            return -1

    num = [p for i,p in enumerate(prime) if perm[i] == '0']
    return ''.join(num)


# check if primes of length have an eight prime family
familySize = 8
# set min and max length of prime numbers
min_length = 6
max_length = 8
# make all perms beforehand
perms = []
perLen =  min_length
# perms with length l and stars s perm in perms[length][stars]
for l in range(min_length,max_length):
    lPerm = []
    for stars in range(1,perLen):
        arr = ['0' for i in range(perLen)]
        # set each replace index to 1
        for i in range(stars):
            arr[i] = '1'
        ps = [''.join(p) for p in permutations(arr)]
        ps = list(set(ps))
        lPerm.append(ps)
    perLen+=1
    perms.append(lPerm)


length = min_length
while length < max_length:
    # empty list
    primes = []
    # read from a premade list of primes
    with open('primes.txt', 'r') as f:
        line = '1'
        while line and length >= len(line):
            line = f.readline().strip()
            # add primes with desired lenght
            if len(line) == length:
                primes.append(line)

    print('Primes loaded')

    for permlen in perms[length-min_length]:# perm in the form of ['1','0','0']
        for perm in permlen:
            print(perm)
            # mask the primes using m
            perm_i = [i for i,v in enumerate(perm) if v == '1']#['1','0','0'] --> [0]
            result = [masking(prime, perm_i) for prime in primes]


            # count the number of instances the different sets have, might be worth implementing this in the masking function
            result = Counter(result)
            if familySize in result.values():
                for num, count in result.items():
                    if count == familySize:
                        print(result)
                        print('----------------')
                        print('Prime part: {}\nPermutation: {}\nCount: {}'.format(num,perm,count))
                # the family has been found, exit program
                end = time.time()
                print('time',(end-start))
                exit()

    length+=1
