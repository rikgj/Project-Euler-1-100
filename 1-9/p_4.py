'''
A palindromic number reads the same both ways. The largest palindrome made from the product of two 2-digit numbers is 9009 = 91 × 99.

Find the largest palindrome made from the product of two 3-digit numbers.
'''
# FIXME: Obviously this should start at the highest value and work its way down...
max = 1000
f1 = 100
f2 = 100
palindromic = -1
while f2 < max:
    f1=100
    while f1 < max:
        n = str(f1*f2)
        nr = n[::-1]
        if(n == nr and int(n) > int(palindromic)):
            palindromic = n
        f1+=1
    f2+=1

print(palindromic)
