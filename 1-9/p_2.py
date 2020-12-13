'''
Each new term in the Fibonacci sequence is generated by adding the previous two terms. By starting with 1 and 2, the first 10 terms will be:

1, 2, 3, 5, 8, 13, 21, 34, 55, 89, ...

By considering the terms in the Fibonacci sequence whose values do not exceed four million, find the sum of the even-valued terms.
'''

# go through the Fibbonacci sequense upp till 4 000 000
a = 1
b = 2
c = a+b
# sum is 2 because b is even
sum = 2

while c < 4000000:
    # add any even number to a sum
    if(c%2==0):
        sum+=c
    #proceed to next value
    a = b
    b = c
    c = a+b


# print sum
print(sum)
