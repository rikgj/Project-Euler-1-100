'''
A permutation is an ordered arrangement of objects. For example, 3124 is one possible permutation of the digits 1, 2, 3 and 4. If all of the permutations are listed numerically or alphabetically, we call it lexicographic order. The lexicographic permutations of 0, 1 and 2 are:

012   021   102   120   201   210

What is the millionth lexicographic permutation of the digits 0, 1, 2, 3, 4, 5, 6, 7, 8 and 9?
'''
import math

set = [0,1,2,3,4,5,6,7,8,9]
goal = 1000000-1 # starts counting at 0
len_s = len(set)
solution = ''

while len_s > 0:
    val = math.factorial(len_s-1)
    i=0
    while goal > 0:
        goal-=val
        if goal >=0:
            i+=1
        elif goal < 0:
            goal+=val
            break

    solution+=str(set.pop(i))
    len_s-=1

print(solution)
