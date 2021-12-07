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
hit_list = []

i = 0
level = 0
player = 'Z'
goal = 'D'
searching = True

initX = ch_dict[goal][1]
initY = ch_dict[goal][0]
startPos = [[initX, initY], level, 'X', 'X']
player_dict = [ch_dict[player][1], ch_dict[player][0]]

if (tempArr2[initY - 1][initX] != '#'):         #initUpCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'U')
    temp_list.insert(len(temp_list)-1, temp_index)
    hit_list.append(temp_index[0:2])

if (tempArr2[initY][initX + 1] != '#'):         #initRightCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'R')
    temp_list.insert(len(temp_list)-1, temp_index)
    hit_list.append(temp_index[0:2])

if (tempArr2[initY + 1][initX] != '#'):         #initDownCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'D')
    temp_list.insert(len(temp_list)-1, temp_index)
    hit_list.append(temp_index[0:2])

if (tempArr2[initY][initX - 1] != '#'):         #initLeftCheck
    temp_index = startPos.copy()
    temp_index.insert(0, 'L')
    temp_list.insert(len(temp_list)-1, temp_index)
    hit_list.append(temp_index[0:2])

level += 1

# ---------------------------------

def leftCheck2(origin):
    global level, player, searching
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y][x - 1 - (2*k)] != '#' and searching):
        if (tempArr2[y][x - 2 - (2*k)] == player):
            #print("foundL")
            #print(tempArr2[y][x - 2 - (2*k)], (x - 2 - (2*k), y), level)
            temp_list.insert( len(temp_list)-1, ["Player", [x - 2 - (2*k), y], level, origin[0], origin[1]] )
            searching = False
            break
        if (tempArr2[y + 1][x - 2 - (2*k)] == '#'):
            mty_list.append(['U', [x - 2 - (2*k), y], level, origin[0], origin[1]])
        if (tempArr2[y - 1][x - 2 - (2*k)] == '#'):
            mty_list.append(['D', [x - 2 - (2*k), y], level, origin[0], origin[1]])
        k += 1

def rightCheck2(origin):
    global level, player, searching
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y][x + 1 + (2*k)] != '#' and searching):
        if (tempArr2[y][x + 2 + (2*k)] == player):
            #print("foundR")
            #print(tempArr2[y][x + 2 + (2*k)], (x + 2 + (2*k), y), level)
            temp_list.insert( len(temp_list)-1, ["Player", [x + 2 + (2*k), y], level, origin[0], origin[1]] )
            searching = False
            break
        if (tempArr2[y + 1][x + 2 + (2*k)] == '#'):
            mty_list.append(['U', [x + 2 + (2*k), y], level, origin[0], origin[1]])
        if (tempArr2[y - 1][x + 2 + (2*k)] == '#'):
            mty_list.append(['D', [x + 2 + (2*k), y], level, origin[0], origin[1]])
        k += 1

def upCheck2(origin):
    global level, player, searching
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y - 1 - (2*k)][x] != '#' and searching):
        if (tempArr2[y - 2 - (2*k)][x] == player):
            #print("foundU")
            #print(tempArr2[y - 2 - (2*k)][x], (x, y - 2 - (2*k)), level)
            temp_list.insert( len(temp_list)-1, ["Player", [x, y - 2 - (2*k)], level, origin[0], origin[1]] )
            searching = False
            break
        if (tempArr2[y - 2 - (2*k)][x + 1] == '#'):
            mty_list.append(['L', [x, y - 2 - (2*k)], level, origin[0], origin[1]])
        if (tempArr2[y - 2 - (2*k)][x - 1] == '#'):
            mty_list.append(['R', [x, y - 2 - (2*k)], level, origin[0], origin[1]])
        k += 1

def downCheck2(origin):
    global level, player, searching
    x = origin[1][0]
    y = origin[1][1]

    k = 0
    while (tempArr2[y + 1 + (2*k)][x] != '#' and searching):
        if (tempArr2[y + 2 + (2*k)][x] == player):
            #print("foundD")
            #print(tempArr2[y + 2 + (2*k)][x], (x, y + 2 + (2*k)), level)
            temp_list.insert( len(temp_list)-1, ["Player", [x, y + 2 + (2*k)], level, origin[0], origin[1]] )
            searching = False
            break
        if (tempArr2[y + 2 + (2*k)][x + 1] == '#'):
            mty_list.append(['L', [x, y + 2 + (2*k)], level, origin[0], origin[1]])
        if (tempArr2[y + 2 + (2*k)][x - 1] == '#'):
            mty_list.append(['R', [x, y + 2 + (2*k)], level, origin[0], origin[1]])
        k += 1

# ---------------------------------

while searching:
    #print(len(hit_list), hit_list)
    if (level == 20):                                    # change search level here
        break
    if (temp_list[i] == 'X'):
        for c in mty_list:
            if (c[0:2] not in hit_list):
                temp_list.insert( len(temp_list)-1, c )
                hit_list.append(c[0:2])
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

paths_list = []
for p in temp_list:
    if (p == 'X'):
        break
    if (p[2] == level):
        paths_list.append(p)

for n in paths_list:
    path = []
    path.append(n[0:3])

    prev_level = level
    while n[2] != 0:
        prev_level -= 1
        prev_n = n[3:5]
        prev_n.append(prev_level)

        temp_cnt = 0
        while temp_list[temp_cnt][0:3] != prev_n:
            temp_cnt += 1
        n = temp_list[temp_cnt]
        path.append(n[0:3])
    for p in path:
        if p[2] == 0:
            p[0] = 'Goal'
        print(str(spaceCnt(level - p[2])) + str(p[0:2]))

'''
for n in temp_list:
    if (n == 'X'):
        break
    print(str(spaceCnt(n[2])) + str(n))
'''

# Branching paths
    # Waitlisted paths
    
                # upcheck [28, 24]
                # leftcheck [28, 6]
# downcheck [12, 6]             # upcheck [4, 6]
# leftcheck [12, 10]


# 1) When path runs into a barrier, it doesn't search for directions from that spot
#       Not an Issue. Working as intended
# 2) [FIXED]
# 3) [FIXED]
# 4) cancel out searches created by corridors
# 5) Implement a stop function when the Player is found