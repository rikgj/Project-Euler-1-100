'''
Surprisingly there are only three numbers that can be written as the sum of fourth powers of their digits:

1634 = 14 + 64 + 34 + 44
8208 = 84 + 24 + 04 + 84
9474 = 94 + 44 + 74 + 44
As 1 = 14 is not a sum it is not included.

The sum of these numbers is 1634 + 8208 + 9474 = 19316.

Find the sum of all the numbers that can be written as the sum of fifth powers of their digits.
'''
import timeit

def powersums():
    num = 2
    power = 5
    winners = []

    # find the sum of the single digits by the power of len(num)
    while num < 355000:
        sum = 0
        num_str = str(num)
        digits = list(num_str)

        for dig in digits:
            sum+= int(dig)**power

        if(sum == num):
            winners.append(num)

        num+=1

    # present the winners
    print("Number of winners: {}\nThe winners:\n{}".format(len(winners), winners))
    sum = 0
    for winner in winners:
        sum+=winner
    print(sum)


powersums()

# execution_time = timeit.timeit(powersums, number=10)
# print(execution_time)
