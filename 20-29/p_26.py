'''
A unit fraction contains 1 in the numerator. The decimal representation of the unit fractions with denominators 2 to 10 are given:

1/2	= 	0.5
1/3	= 	0.(3)
1/4	= 	0.25
1/5	= 	0.2
1/6	= 	0.1(6)
1/7	= 	0.(142857)
1/8	= 	0.125
1/9	= 	0.(1)
1/10	= 	0.1
Where 0.1(6) means 0.166666..., and has a 1-digit recurring cycle. It can be seen that 1/7 has a 6-digit recurring cycle.

Find the value of d < 1000 for which 1/d contains the longest recurring cycle in its decimal fraction part.
'''


from decimal import *

# the winner d and its cycle length
winner_len = -1
winner_d = -1
# FIXME: problem at d=202
# FIXME: problem at d=505

d =1
while d < 1000:
    #print(d)
    if(d == 202 or d == 505):
        #print("BAD VALUE {} SKIP".format(d))
        d+=1

    # set number of decimals to include
    max_decimals = 30


    found = False
    pattern_size = 1
    while not found:
        getcontext().prec = max_decimals
        res = str(Decimal(1)/Decimal(d))
        # selecting decimal part of number and cutting out the last number because of rounding
        res = res[2:-1]
        digit_len = len(res)
        pattern = ""
        if digit_len > 10:
            # look for pattern
            pattern_index = digit_len - pattern_size
            pattern = res[pattern_index:]
            # find potential match from back to front
            match_index = res.rfind(pattern, 0, pattern_index)
            if(match_index == -1):
                max_decimals+=20
            else:
                # find excess, space between match_index and pattern
                excess = pattern_index - (match_index + pattern_size)
                pattern_size+= excess

                if excess == 0 and match_index != -1:
                    found = True
                    #print(pattern)
                elif (pattern_size*2+5 > digit_len):
                    max_decimals = pattern_size*2+5

        else:
            found = True

    if len(pattern) > winner_len:
        # we found a pattern and it is better than what we alreaddy have
        winner_len = len(pattern)
        winner_d = d
        #print("---\nd -- {}\nlen -- {}".format(winner_d,winner_len))


    d+=1

print("\nwinner_d -- {}\nwinner_len -- {}".format(winner_d,winner_len))
