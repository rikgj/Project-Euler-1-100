'''
A Pythagorean triplet is a set of three natural numbers, a < b < c, for which,

a2 + b2 = c2
For example, 3^2 + 4^2 = 9 + 16 = 25 = 5*2.

There exists exactly one Pythagorean triplet for which a + b + c = 1000.
Find the product abc.
'''
import math
a = 3
found = False

while (not found):

    b = a + 1
    while(b < 600 and not found):
        b += 1
        c =  math.sqrt(a**2 + b**2)
        sum = a + b + c

        if(sum == 1000 and c.is_integer()):
            abc = a*b*c
            print("FOUND! \na = {}, b = {}, c = {}, abc = {}".format(a,b,c,abc))
            found = True
    a+=1
