'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''

min = 100
f1 = 1000
f2 = 1000
palindromic = -1 # all positive numbers are greater than -1
while f2 > min:
    f1=1000
    found = False
    while f1 > min and not found:
        # convert product to string
        n = str(f1*f2)
        # reverse the string
        nr = n[::-1]
        # check if palindromic
        if(n == nr and int(n) > int(palindromic)):
            palindromic = n
            # this is the greatest palindrome with current f1
            found = True
        f1-=1
    f2-=1

print(palindromic)
