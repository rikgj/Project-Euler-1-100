'''
The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?
'''

# find the factors of num using modulus operator
num = 600851475143
div = 2
highestFactor = 1

while num > 1:
    if(num%div==0):
        num = num/div
        highestFactor = div
    else:
        div+=1
print(highestFactor)
