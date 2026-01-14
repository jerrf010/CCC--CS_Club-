x = int(input("Enter x value: "))
y = int(input("Enter y value: "))

if x < 0 and y < 0:
    print("Third Quadrant")
elif x < 0 and y > 0:
    print("Second Quadrant")
elif x > 0 and y < 0:
    print("Fourth Quadrant")
elif x > 0 and y > 0:
    print("First Quadrant")
else:
    print("On an axis")