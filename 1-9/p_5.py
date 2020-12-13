'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

# no need to check n < 2520
n = 2520
found = False
# check divisibility in the range 11 --> 19
div = 11
while (not found):
    if(n%div==0):
        if(div==19):
            found = True
        else:
            div+=1
    else:
        div = 11
        #no need to check more than every 20th number
        n+=20
print(n)
