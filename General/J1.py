wins = 0

for i in range(6):
    i = str(input("W or L \n")).lower()
    if i == "w":
        wins += 1
if wins == 5 or wins == 6:
    print("Group 1")
elif wins == 3 or wins == 4:
    print("Group 2")
elif wins == 1 or wins == 2:
    print("Group 3")
elif wins == 0:
    print("no group")
