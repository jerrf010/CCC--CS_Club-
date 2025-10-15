d = int(input("Starting Size: "))
r = d
while True:
    yobiSize = int(input("Yobi Size: "))
    if d <= yobiSize:
        print(r)
        break
    elif d > yobiSize:
        r = d + yobiSize