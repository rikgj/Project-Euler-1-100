'''

By starting at the top of the triangle below and moving to adjacent numbers on the row below, the maximum total from top to bottom is 23.

3
7 4
2 4 6
8 5 9 3

That is, 3 + 7 + 4 + 9 = 23.

Find the maximum total from top to bottom of the triangle below:

NOTE: As there are only 16384 routes, it is possible to solve this problem by trying every route. However, Problem 67, is the same challenge with a triangle containing one-hundred rows; it cannot be solved by brute force, and requires a clever method! ;o)
'''

txt = '''75
95 64
17 47 82
18 35 87 10
20 04 82 47 65
19 01 23 75 03 34
88 02 77 73 07 63 67
99 65 04 28 06 16 70 92
41 41 26 56 83 40 80 70 33
41 48 72 33 47 32 37 16 94 29
53 71 44 65 25 43 91 52 97 51 14
70 11 33 28 77 73 17 78 39 68 17 57
91 71 52 38 17 14 91 43 58 50 27 29 48
63 66 04 68 89 53 67 30 73 16 69 87 40 31
04 62 98 27 23 09 70 98 73 93 38 53 60 04 23'''

# make string to a working array
oldarr = txt.split('\n')
arr = []
for index_l, list in enumerate(oldarr):
    list = list.split()
    arr.append([])
    for val in list:
        val = int(val)
        arr[index_l].append(val)


# compare two values and return result
def compare(val0, val1):
    if( not (isinstance(val0, int) or isinstance(val1, int))):
        print("compare value not int")
    if(val0 >= val1):
        return (0,"0",val0)
    else:
        return (1,"1",val1)

# path finding
max_step = len(arr)
memory = [] # remember paths you do not want to go
bestpos = 83 # not a realistic value
winner = -1

c_step = 1
c_val = arr[0][0]
c_path = "0"
choice = 0

while c_step <= max_step:
    # choose between the next two paths
    val0 = arr[c_step][choice]
    val1 = arr[c_step][(choice+1)]
    res = compare(val0, val1)
    test_path = c_path
    test_path+=res[1]

    if(test_path in memory):
        # make another choice
        if res[0] == 0:
            res = (1,"1",val1)

        elif res[0] == 1:
            res = (0,"0",val0)

    choice+=res[0]
    c_path+=res[1]
    c_val+=res[2]
    c_step+=1

    # check if next/new path is possible
    bestoutcome = c_val + bestpos * (max_step - c_step)
    if((bestoutcome < winner) or (c_step == max_step)):
        if(c_val > winner):
            winner = c_val
            print("current winner: {}".format(winner))

        memory.append(c_path)

        # check for alternative path
        found = False
        while not found:
            c_path = c_path[0:-1]
            if(len(c_path) > 0):
                # add bad branch to memory if present
                if (((c_path + "0") in memory) and ((c_path + "1") in memory)):
                    memory.append(c_path)

                if(c_path not in memory):
                    found = True
                    # set values to current path
                    progress = len(c_path)
                    i = 0
                    c_val = 0
                    choice = 0
                    while i < progress:
                        k = int(c_path[i])
                        choice+=k
                        c_val+=arr[i][choice]
                        i+=1

                    c_step = progress
            else:
                #no alt path found, all paths have been checked?
                c_step = max_step+1
                found = True


# reveal the winner
print("The best value is {}".format(winner))
print(len(memory))
