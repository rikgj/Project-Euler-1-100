'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.

What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
'''

n = 2520
found = False
# no need to check n%1
div = 2
while (not found):
    if(n%div==0):
        if(div==20):
            found = True
        else:
            div+=1
    else:
        div = 2
        #no need to check more than every 20th number
        n+=20
print(n)
