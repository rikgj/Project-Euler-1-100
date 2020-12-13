'''
2*15 = 32768 and the sum of its digits is 3 + 2 + 7 + 6 + 8 = 26.

What is the sum of the digits of the number 2**1000
'''

# take the sum of the digits in the string of 2**1000
numSum = sum([int(x) for x in str(2**1000)])
print(numSum)
