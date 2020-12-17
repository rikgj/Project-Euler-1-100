'''
We shall say that an n-digit number is pandigital if it makes use of all the digits 1 to n
 exactly once; for example, the 5-digit number, 15234, is 1 through 5 pandigital.

The product 7254 is unusual, as the identity, 39 × 186 = 7254, containing multiplicand,
multiplier, and product is 1 through 9 pandigital.

Find the sum of all products whose multiplicand/multiplier/product identity can
be written as a 1 through 9 pandigital.

HINT: Some products can be obtained in more than one way so be sure to only
include it once in your sum.
'''

# store the found pans
pans = []
a = 2
b = 0

while a < 987:
    # update b and c
    b+=1
    c = a*b
    # get the string concat of abc, so that we can easily check the values
    totstr = str(a) + str(b) + str(c)

    # check if it has the right length 1-9 --> len = 9
    length = len(totstr)
    if length == 9 and '0' not in totstr:
        # make a list of the string in int
        d_arr = [int(x) for x in totstr]
        # sort in increasing order
        d_arr.sort()
        good = True
        # check if the list is 1,2,3,4,5,6,7,8,9
        for i,x in enumerate(d_arr):
            if x != i+1:
                good = False
                break
        # add if not alreaddy there
        if good and c not in pans:
            pans.append(c)


    elif length > 9 or len(str(b)) > 4:
        print(a)# just to see progress
        a+=1
        b=0


# print the sum of the found pans
print('------------')
print(pans)
print(sum(pans))
