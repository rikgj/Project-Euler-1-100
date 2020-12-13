'''
The sum of the squares of the first ten natural numbers is,

1^2+2^2+...+10^2 = 385
The square of the sum of the first ten natural numbers is,

(1+2+...+10)^2 = 55^2 = 3025
Hence the difference between the sum of the squares of the first ten natural numbers and the square of the sum is 3025−385=2640.

Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

limit = 100
#sum natural numbers squared
i = 0
s1 = 0
while i <=limit:
    s1+=i**2
    i+=1
#sum of the natural numbers sum, squared
s2=0
i = 0
while i <= limit:
    s2+=i
    i+=1
s2 = s2**2

diff = s2-s1
print(diff)
