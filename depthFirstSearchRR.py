# open a file
file = open('DefaultMap.txt', 'r')

# create some preliminary things
ch_list = ['V','W','Y','Z','A','B','C','D','E','F','G','H','I','J','K','L','M','N','P','Q','R']
ch_dict = {}

tempArr2 = []
for posy, l_num in enumerate(file):             # for every row
    tempArr1 = []
    for posx, c_num in enumerate(l_num):        # for every column
        tempArr1.append(c_num)
        if c_num in ch_list:                    # if a letter is found
            ch_dict[c_num] = [posx, posy]       # write into a dict
            # print(ch_dict)
    tempArr2.append(tempArr1[:-1])              # removed Newline characters



# right vertical check
def rightCheck(ch = '9', x = -1, y = -1):
    global cnt, recur
    if (x == -1 & y == -1):
        x = ch_dict.get(ch)[0]
        y = ch_dict.get(ch)[1]
        print(x, y)
    i = 0
    while (tempArr2[y][x + 1 + (2 * i)] != '#'):                # checking if we reach the end of our branch
        # 
        #  'V'[#]
        # 
        if (tempArr2[y + 1][x + 2 + (2 * i)] == '#'):           # checking for a branch coming from above
            #
            #  'V''_''O'
            #     '#'[#]'#'
            # 
            print( "\tup check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x + 2 + (2 * i), y] )           # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                upCheck(x = x + 2 + (2 * i), y = y)                     # recursion call
                cnt -= 1
        elif (tempArr2[y - 1][x + 2 + (2 * i)] == '#'):         # checking for a branch coming from below
            #
            #     '#'[#]'#'
            #  'V''_''O'
            # 
            print( "\tdown check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x + 2 + (2 * i), y] )         # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                downCheck(x = x + 2 + (2 * i), y = y)                   # recursion call
                cnt -= 1
        i += 1
    print("\tright break:{}{}".format("\t" + str(cnt), " " + spaceCnt()) + str(x + (2 * i)) , str(y))

# left horizontal check
def leftCheck(ch = '9', x = -1, y = -1):
    global cnt, recur
    if (x == -1 & y == -1):
        x = ch_dict.get(ch)[0]
        y = ch_dict.get(ch)[1]
        print(x, y)
    i = 0
    while (tempArr2[y][x - 1 - (2 * i)] != '#'):                # checking if we reach the end of our branch
        # 
        #  [#]'V'
        # 
        if (tempArr2[y + 1][x - 2 - (2 * i)] == '#'):           # checking for a branch coming from above
            #
            #     'O''_''V'
            #  '#'[#]'#'
            # 
            print( "\tup check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x - 2 - (2 * i), y] )           # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                upCheck(x = x - 2 - (2 * i), y = y)                     # recursion call
                cnt -= 1
        elif (tempArr2[y - 1][x - 2 - (2 * i)] == '#'):         # checking for a branch coming from below
            #
            #  '#'[#]'#'
            #     'O''_''V'
            # 
            print( "\tdown check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x - 2 - (2 * i), y] )         # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                downCheck(x = x - 2 - (2 * i), y = y)                   # recursion call
                cnt -= 1
        i += 1
    print("\tleft break:{}{}".format("\t" + str(cnt), " " + spaceCnt()) + str(x - (2 * i)) , str(y))

# downwards vertical check
def downCheck(ch = '9', x = -1, y = -1):
    global cnt, recur
    if (x == -1 & y == -1):
        x = ch_dict.get(ch)[0]
        y = ch_dict.get(ch)[1]
        print(x, y)
    i = 0
    while (tempArr2[y + 1 + (2 * i)][x] != '#'):                # checking if we reach the end of our branch
        # 
        #     'V'
        #     [#]
        # 
        if (tempArr2[y + 2 + (2 * i)][x + 1] == '#'):           # checking for a branch coming from the left
            #
            #     'V'
            #     '_' '#'
            #     'O' [#]
            #         '#'
            # 
            print( "\tleft check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x, y + 2 + (2 * i)] )         # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                leftCheck(x = x, y = y + 2 + (2 * i))                   # recursion call
                cnt -= 1
        elif (tempArr2[y + 2 + (2 * i)][x - 1] == '#'):         # checking for a branch coming from the right
            #
            #         'V'
            #     '#' '_'
            #     [#] 'O'
            #     '#'
            # 
            print( "\tright check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x, y + 2 + (2 * i)] )        # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                rightCheck(x = x, y = y + 2 + (2 * i))                  # recursion call
                cnt -= 1
        i += 1
    print("\tdown break:{}{}".format("\t" + str(cnt), " " + spaceCnt()) + str(x) , str(y + (2 * i)))

# upwards vertical check
def upCheck(ch = '9', x = -1, y = -1):
    global cnt, recur
    if (x == -1 & y == -1):
        x = ch_dict.get(ch)[0]
        y = ch_dict.get(ch)[1]
        print(x, y)
    i = 0
    while (tempArr2[y - 1 - (2 * i)][x] != '#'):                # checking if we reach the end of our branch
        # 
        #     [#]
        #     'V'
        # 
        if (tempArr2[y - 2 - (2 * i)][x + 1] == '#'):           # checking for a branch coming from the left
            #
            #         '#'
            #     'O' [#]
            #     '_' '#'
            #     'V'
            # 
            print( "\tleft check:{}{}".format("\t" + str(cnt), spaceCnt()), [x, y - 2 - (2 * i)] )         # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                leftCheck(x = x, y = y - 2 - (2 * i))                   # recursion call
                cnt -= 1
        elif (tempArr2[y - 2 - (2 * i)][x - 1] == '#'):         # checking for a branch coming from the right
            #
            #     '#'    
            #     [#] 'O'
            #     '#' '_'
            #         'V'
            # 
            print( "\tright check:{}{}".format("\t" + str(cnt), spaceCnt()) , [x, y - 2 - (2 * i)] )        # returns the coords of char 'O'
            if (cnt < recur):
                cnt += 1
                rightCheck(x = x, y = y - 2 - (2 * i))                  # recursion call
                cnt -= 1
        i += 1
    print("\tup break:{}{}".format("\t" + str(cnt), " " + spaceCnt()) + str(x) , str(y - (2 * i)))

def spaceCnt():
    global cnt
    spaces = ""
    for i in range(cnt):
        spaces += " "
    return spaces

cnt = 0
recur = 4
upCheck(ch = 'D')