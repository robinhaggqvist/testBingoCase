import random

maxRnd = 25

user = [
[(0, 1), (0, 0), (0, 0), (0, 0), (0, 1)],
[(0, 0), (0, 1), (0, 0), (0, 1), (0, 0)],
[(0, 0), (0, 0), (0, 1), (0, 0), (0, 0)],
[(0, 0), (0, 1), (0, 0), (0, 1), (0, 0)],
[(0, 1), (0, 0), (0, 0), (0, 0), (0, 1)]]

def fillRandom(usr):
    rndlist = []
    while len(rndlist)<17:
        rndTemp = random.randint(1,maxRnd)
        if rndTemp not in rndlist:
            rndlist.append(rndTemp)
    usr[0][1] = (rndlist[0],0)
    usr[0][2] = (rndlist[1],0)
    usr[0][3] = (rndlist[2],0)
    usr[1][0] = (rndlist[3],0)
    usr[1][2] = (rndlist[4],0)
    usr[1][4] = (rndlist[5],0)
    usr[2][0] = (rndlist[6],0)
    usr[2][1] = (rndlist[7],0)
    usr[2][3] = (rndlist[8],0)
    usr[2][4] = (rndlist[9],0)
    usr[3][0] = (rndlist[10],0)
    usr[3][2] = (rndlist[11],0)
    usr[3][4] = (rndlist[12],0)
    usr[4][1] = (rndlist[13],0)
    usr[4][2] = (rndlist[14],0)
    usr[4][3] = (rndlist[15],0)

def checkNumber(check,usr):
#    print(f'random int: {check}')
    for i in range(0,5):
        for j in range(0,5):
#            print(f'i: {i} j: {j} check: {usr[i][j][0]} ')
            if usr[i][j][0] == check:
                usr[i][j] = (usr[i][j][0],1)

def checkWin(usr):
    for i in range(0,4):
        if usr[i][0][1] == 1 and usr[i][1][1] == 1 and usr[i][2][1] == 1 and usr[i][3][1] == 1 and usr[i][4][1] == 1:
            return True
    
    for i in range(0,4):
        if usr[0][i][1] == 1 and usr[1][i][1] == 1 and usr[2][i][1] == 1 and usr[3][i][1] == 1 and usr[4][i][1] == 1:
            return True
    return False


u1 = user
fillRandom(u1)

for i in range(1,100):
    checkNumber(random.randint(1,maxRnd),u1)
    if checkWin(u1):
        print(f'Numbers drawn: {i+1}')
        break
    print('No win')


# print(f'u1[0]: {u1[0]}')
# print(f'u1[1]: {u1[1]}')
# print(f'u1[2]: {u1[2]}')
# print(f'u1[3]: {u1[3]}')
# print(f'u1[4]: {u1[4]}')

#print(f'Checkwin(u1): {checkWin(u1)}')
