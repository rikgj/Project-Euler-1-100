'''
n! means n × (n − 1) × ... × 3 × 2 × 1

For example, 10! = 10 × 9 × ... × 3 × 2 × 1 = 3628800,
and the sum of the digits in the number 10! is 3 + 6 + 2 + 8 + 8 + 0 + 0 = 27.

Find the sum of the digits in the number 100!

'''

n = 100
sum = 1
while n > 0:
    sum*=n
    n-=1

sum = str(sum)
ans = 0
for c in sum:
    ans+=int(c)

print(ans)
