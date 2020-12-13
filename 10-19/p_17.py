'''
If the numbers 1 to 5 are written out in words: one, two, three, four, five, then there are 3 + 3 + 5 + 4 + 4 = 19 letters used in total.

If all the numbers from 1 to 1000 (one thousand) inclusive were written out in words, how many letters would be used?

NOTE: Do not count spaces or hyphens.

For example:
342 (three hundred and forty-two) contains 23 letters
115 (one hundred and fifteen) contains 20 letters.
The use of "and" when writing out numbers is in compliance with British usage.
'''
# define the written numbers in a list
lowernumbers = [
    "ZERO", "one", "two","three","four","five","six","seven","eight","nine","ten",
    "eleven","twelve","thirteen","fourteen","fifteen","sixteen","seventeen", "eighteen", "nineteen"
]

tens = [
    "ZERO","TEN","twenty","thirty","forty","fifty","sixty","seventy","eighty","ninety"
]

hund = "hundred"

def numToText(num):
    # translate a number to text 1-999
    numstr = str(num)
    res = ""
    length = len(numstr)
    done = False

    # add hundreds 100-900
    if(length == 3):
        hun = int(numstr[length -3])
        res+=lowernumbers[hun] + hund
        if(num-100*hun>0):
            res+="and"

    # add tens 20-90 and 10-19
    if(length >= 2 and numstr[length-2] != '0'):
        ten = int(numstr[length-2])
        if ten > 1:
            res+=tens[ten]
        else:
            ten = ten*10 + int(numstr[length-1])
            res+=lowernumbers[ten]
            done = True

    # add 1-9
    if(not done and numstr[length-1] != '0'):
        low = int(numstr[length-1])
        res+=lowernumbers[low]

    return res


counter = 1
numofchars = 0
while counter < 1000:
    text = numToText(counter)
    print(text)
    numofchars+=len(text)
    counter+=1

# add 1000
numofchars+=len("onethousand")
print(numofchars)
