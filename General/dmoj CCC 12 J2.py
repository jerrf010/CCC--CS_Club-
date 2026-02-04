angles = []

for i in range(3):
    reading = int(input())
    angles.append(reading)

if sum(angles) != 180:
    print("error")

elif angles[1] == angles[2] == angles[3]:
    print("Equilateral")

