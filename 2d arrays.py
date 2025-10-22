arr = []
distance = []
for i in range(4):
    i = int(input("Enter a number: "))
    arr.append(i)

for f in range(3):
    distance.append(arr[f]+arr[f+1])

print(distance)