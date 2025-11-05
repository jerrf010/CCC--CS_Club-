magic = True

sqaure = []

for i in range(4):
    row = list(map(int,input().split()))
    sqaure.append(row)

target_sum = sqaure[0][0] + sqaure[0][1] + sqaure[0][2] + sqaure[0][3]

for row in range(4):
    rowSum = 0
    for col in range(4):
        rowSum += sqaure[row][col]
    if rowSum != target_sum:
        magic = False
        break
    
if magic == False:
    print("not magic")

else:
    for col in range(4):
        colSum = 0
        for row in range(4):
            colSum += sqaure[row][col]
        if colSum != target_sum:
            magic = False
            break

    if magic  == False:
        print("not magic")
    if magic == True:
        print("magic")