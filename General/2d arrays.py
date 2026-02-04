arr = [[16,3,2,13],[5,10,11,8],[9,6,7,12],[4,15,14,1]]
counter = 0
rowsum = [0,0,0,0]
for i in range(4):
    for f in range(4):
        rowsum[i] += arr[i][f]

    if rowsum[i] == 34:
        counter += 1
    for j in range(4):
        colsum = 0
        for k in range(4):
            colsum += arr[k][j]
        if colsum == 34:
            counter += 1

if counter == 8:
    print("Magic Square")