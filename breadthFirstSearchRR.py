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
            ch_dict[c_num] = [posy, posx]       # write into a dict
            #print(ch_dict)
    tempArr2.append(tempArr1[:-1])              # removed Newline characters

temp_list = ['X']
mty_list = []
#hit_list = []

i = 0
level = 0
player = 'Y'
goal = 'H'

initX = ch_dict[goal][1]
initY = ch_dict[goal][0]
startPos = [[initY, initX], level, 'X', 'X']

if (tempArr2[initY - 1][initX] != '#'):         #initUpCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'U')
    temp_list.insert(len(temp_list)-1, temp_index)
    #hit

if (tempArr2[initY][initX + 1] != '#'):         #initRightCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'R')
    temp_list.insert(len(temp_list)-1, temp_index)

if (tempArr2[initY + 1][initX] != '#'):         #initDownCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'D')
    temp_list.insert(len(temp_list)-1, temp_index)

if (tempArr2[initY][initX - 1] != '#'):         #initLeftCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'L')
    temp_list.insert(len(temp_list)-1, temp_index)

level += 1

# ---------------------------------

def leftCheck2(origin):
    global level
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y][x - 1 - (2*k)] != '#'):
        if (tempArr2[y + 1][x - 2 - (2*k)] == '#'):
            mty_list.append(['U', [x - 2 - (2*k), y], level, origin[0], origin[1]])
        if (tempArr2[y - 1][x - 2 - (2*k)] == '#'):
            mty_list.append(['D', [x - 2 - (2*k), y], level, origin[0], origin[1]])
        k += 1

def rightCheck2(origin):
    global level
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y][x + 1 + (2*k)] != '#'):
        if (tempArr2[y + 1][x + 2 + (2*k)] == '#'):
            mty_list.append(['U', [x + 2 + (2*k), y], level, origin[0], origin[1]])
        if (tempArr2[y - 1][x + 2 + (2*k)] == '#'):
            mty_list.append(['D', [x + 2 + (2*k), y], level, origin[0], origin[1]])
        k += 1

def upCheck2(origin):
    global level
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y - 1 - (2*k)][x] != '#'):
        if (tempArr2[y - 2 - (2*k)][x + 1] == '#'):
            mty_list.append(['U', [x, y - 2 - (2*k)], level, origin[0], origin[1]])
        if (tempArr2[y - 2 - (2*k)][x - 1] == '#'):
            mty_list.append(['D', [x, y - 2 - (2*k)], level, origin[0], origin[1]])
        k += 1

def downCheck2(origin):
    global level
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y + 1 + (2*k)][x] != '#'):
        if (tempArr2[y + 2 + (2*k)][x + 1] == '#'):
            mty_list.append(['U', [x, y + 2 + (2*k)], level, origin[0], origin[1]])
        if (tempArr2[y + 2 + (2*k)][x - 1] == '#'):
            mty_list.append(['D', [x, y + 2 + (2*k)], level, origin[0], origin[1]])
        k += 1

# ---------------------------------

while temp_list[i] != ch_dict[player]:
    if (level == 2):
        break
    if (temp_list[i] == 'X'):
        for c in mty_list:
            temp_list.insert( len(temp_list)-1, c )
        mty_list = []
        level += 1
    
    if (temp_list[i][0] == 'L'):
        leftCheck2(temp_list[i])
    elif (temp_list[i][0] == 'R'):
        rightCheck2(temp_list[i])
    elif (temp_list[i][0] == 'U'):
        upCheck2(temp_list[i])
    elif (temp_list[i][0] == 'D'):
        downCheck2(temp_list[i])
    i += 1

    #print("\t" + str(temp_list[0]))

def spaceCnt(level):
    spaces = ""
    for i in range(level):
        spaces += "  "
    return spaces

#print(temp_list)

for n in temp_list:
    print(str(spaceCnt(n[2])) + str(n))

# Branching paths
    # Waitlisted paths
    
                # upcheck [28, 24]
                # leftcheck [28, 6]
# downcheck [12, 6]             # upcheck [4, 6]
# leftcheck [12, 10]